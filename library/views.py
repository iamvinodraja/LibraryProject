# views.py
# Put this file in your library app folder

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author, Book, Member, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, MemberSerializer, BorrowRecordSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        # Get only books that have available copies
        available_books = Book.objects.filter(available_copies__gt=0)
        serializer = self.get_serializer(available_books, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def borrow(self, request, pk=None):
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
    
    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
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


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    @action(detail=True, methods=['get'])
    def borrowed_books(self, request, pk=None):
        member = self.get_object()
        active_borrows = BorrowRecord.objects.filter(member=member, return_date__isnull=True)
        serializer = BorrowRecordSerializer(active_borrows, many=True)
        return Response(serializer.data)


class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        # Get all books that haven't been returned yet
        active_borrows = BorrowRecord.objects.filter(return_date__isnull=True)
        serializer = self.get_serializer(active_borrows, many=True)
        return Response(serializer.data)
