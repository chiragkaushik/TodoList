from django.db import models

# Create your models here.

class user(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class TodoList(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length =  30)
    created_by = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Access(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    list_id = models.ForeignKey(TodoList,on_delete=models.CASCADE)
    permission_type = models.CharField(max_length=30)

class TodoItem(models.Model):
    id = models.IntegerField(primary_key = True)
    list_id = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    heading = models.CharField(max_length=30)
    scheduled_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
