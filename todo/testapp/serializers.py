from rest_framework import  serializers
from .models import user, TodoList, Access, TodoItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'first_name', "last_name", "username", "password", "created_at", "updated_at"]

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ["id", "name", "created_by", "created_at", "updated_at"]

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = ['id', 'user_id', 'list_id', 'permission_type']

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'list_id', "heading", "scheduled_on", "created_on", "updated_on"]