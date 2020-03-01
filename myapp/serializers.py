from rest_framework import serializers
from myapp.models import Book, User
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',)
 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'is_rent', 'created_at', 'updated_at')
