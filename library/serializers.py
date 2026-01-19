# serializers.py
# Put this file in your library app folder

from rest_framework import serializers
from .models import Author, Book, Member, BorrowRecord


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'isbn', 'total_copies', 'available_copies']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'phone', 'membership_date']


class BorrowRecordSerializer(serializers.ModelSerializer):
    # book_title = serializers.CharField(source='book.title', read_only=True)
    # member_name = serializers.CharField(source='member.name', read_only=True)
    
    class Meta:
        model = BorrowRecord
        fields = ['id', 'book',  'member', 'borrow_date', 'return_date']
        
# Additional serializers for user registration and details

from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords don't match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user details."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']
        read_only_fields = ['id', 'is_active']