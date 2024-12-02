from django.shortcuts import render

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound

class TaskViewSet(viewsets.ModelViewSet):
    ...
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Task.DoesNotExist:
            raise NotFound(detail="Task not found")

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # فقط کاربران احراز هویت شده می‌توانند وظایف را ویرایش یا حذف کنند

    def perform_create(self, serializer):
        # وقتی که وظیفه جدید اضافه می‌شود، کاربر را از طریق احراز هویت به آن اضافه می‌کنیم.
        serializer.save(user=self.request.user)

