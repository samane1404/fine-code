from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from todo.models import Task

class ToDoAPITestCase(APITestCase):

    def setUp(self):
        # ایجاد یک کاربر جدید برای تست
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  # ورود به حساب کاربری

        # ایجاد یک وظیفه برای این کاربر
        self.task_data = {
            'title': 'Test Task',
            'description': 'This is a test task.',
            'status': 'Pending'
        }
        self.create_url = '/api/tasks/'
        self.task = Task.objects.create(user=self.user, **self.task_data)

    def test_create_task(self):
        """ تست ایجاد یک وظیفه جدید """
        response = self.client.post(self.create_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.task_data['title'])
        self.assertEqual(response.data['status'], self.task_data['status'])

    def test_read_tasks(self):
        """ تست خواندن لیست وظایف """
        response = self.client.get(self.create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.task.title)

    def test_update_task(self):
        """ تست به‌روزرسانی وضعیت یک وظیفه """
        update_data = {'status': 'Completed'}
        url = f'/api/tasks/{self.task.id}/'  # مسیر وظیفه خاص
        response = self.client.put(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Completed')

    def test_delete_task(self):
        """ تست حذف یک وظیفه """
        url = f'/api/tasks/{self.task.id}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # اطمینان حاصل می‌کنیم که وظیفه از پایگاه داده حذف شده است
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_unauthenticated_access(self):
        """ تست دسترسی بدون احراز هویت """
        # ورود به حساب کاربری
        self.client.logout()
        response = self.client.get(self.create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # باید دسترسی غیرمجاز باشد

    def test_create_task_unauthenticated(self):
        """ تست ایجاد وظیفه بدون احراز هویت """
        # ورود به حساب کاربری
        self.client.logout()
        response = self.client.post(self.create_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # باید دسترسی غیرمجاز باشد
