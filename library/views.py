# views.py
# Put this file in your library app folder

from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Author, Book, Member, BorrowRecord
from .serializers import (
    AuthorSerializer, BookSerializer, MemberSerializer, 
    BorrowRecordSerializer, UserRegistrationSerializer, UserSerializer
)
from .permissions import IsAuthenticatedOrReadOnly, IsBorrowerOrAdmin


@extend_schema_view(
    list=extend_schema(description='List all authors'),
    create=extend_schema(description='Create a new author'),
    retrieve=extend_schema(description='Get author details'),
    update=extend_schema(description='Update an author'),
    partial_update=extend_schema(description='Partially update an author'),
    destroy=extend_schema(description='Delete an author'),
)
class AuthorViewSet(viewsets.ModelViewSet):
    """API endpoint for managing authors."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@extend_schema_view(
    list=extend_schema(description='List all books'),
    create=extend_schema(description='Create a new book'),
    retrieve=extend_schema(description='Get book details'),
    update=extend_schema(description='Update a book'),
    partial_update=extend_schema(description='Partially update a book'),
    destroy=extend_schema(description='Delete a book'),
)
class BookViewSet(viewsets.ModelViewSet):
    """API endpoint for managing books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @extend_schema(description='Get all available books (with copies > 0)')
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get only books that have available copies."""
        available_books = Book.objects.filter(available_copies__gt=0)
        serializer = self.get_serializer(available_books, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        description='Borrow a book (requires authentication)',
        request={'member_id': int},
    )
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def borrow(self, request, pk=None):
        """Borrow a book for a member."""
        book = self.get_object()
        member_id = request.data.get('member_id')
        
        if not member_id:
            return Response({'error': 'member_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            member = Member.objects.get(id=member_id)
        except Member.DoesNotExist:
            return Response({'error': 'Member not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if book.available_copies <= 0:
            return Response({'error': 'No copies available'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create borrow record
        BorrowRecord.objects.create(book=book, member=member)
        
        # Decrease available copies
        book.available_copies -= 1
        book.save()
        
        return Response({'message': f'{member.name} borrowed {book.title}'}, status=status.HTTP_200_OK)
    
    @extend_schema(
        description='Return a borrowed book (requires authentication)',
        request={'member_id': int},
    )
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def return_book(self, request, pk=None):
        """Return a borrowed book."""
        book = self.get_object()
        member_id = request.data.get('member_id')
        
        if not member_id:
            return Response({'error': 'member_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            borrow_record = BorrowRecord.objects.filter(
                book=book, 
                member_id=member_id, 
                return_date__isnull=True
            ).first()
            
            if not borrow_record:
                return Response({'error': 'No active borrow record found'}, status=status.HTTP_404_NOT_FOUND)
            
            # Mark as returned
            from django.utils import timezone
            borrow_record.return_date = timezone.now().date()
            borrow_record.save()
            
            # Increase available copies
            book.available_copies += 1
            book.save()
            
            return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(description='List all members'),
    create=extend_schema(description='Register a new member'),
    retrieve=extend_schema(description='Get member details'),
    update=extend_schema(description='Update a member'),
    partial_update=extend_schema(description='Partially update a member'),
    destroy=extend_schema(description='Delete a member'),
)
class MemberViewSet(viewsets.ModelViewSet):
    """API endpoint for managing library members."""
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @extend_schema(description='Get all books currently borrowed by this member')
    @action(detail=True, methods=['get'])
    def borrowed_books(self, request, pk=None):
        """Get member's currently borrowed books."""
        member = self.get_object()
        active_borrows = BorrowRecord.objects.filter(member=member, return_date__isnull=True)
        serializer = BorrowRecordSerializer(active_borrows, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(description='List all borrow records'),
    create=extend_schema(description='Create a new borrow record'),
    retrieve=extend_schema(description='Get borrow record details'),
    update=extend_schema(description='Update a borrow record'),
    partial_update=extend_schema(description='Partially update a borrow record'),
    destroy=extend_schema(description='Delete a borrow record'),
)
class BorrowRecordViewSet(viewsets.ModelViewSet):
    """API endpoint for managing borrow records."""
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsBorrowerOrAdmin]
    
    @extend_schema(description='Get all active borrows (not yet returned)')
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all books that haven't been returned yet."""
        active_borrows = BorrowRecord.objects.filter(return_date__isnull=True)
        serializer = self.get_serializer(active_borrows, many=True)
        return Response(serializer.data)


# Authentication Views
@extend_schema(
    description='Register a new user',
    request=UserRegistrationSerializer,
    responses={201: UserSerializer}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Register a new user account."""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    description='Get current user profile',
    responses={200: UserSerializer}
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """Get the authenticated user's profile."""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)