from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book


class BookCRUDPermissionTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.book = Book.objects.create(
            title='Django',
            author='Astha'
        )

    def test_anyone_can_view_books(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_can_create_book(self):
        self.client.login(username='testuser', password='testpass123')

        response = self.client.post(reverse('book_create'), {
            'title': 'Life',
            'author': 'Ash'
        })

        self.assertTrue(Book.objects.filter(title='AI').exists())

    def test_logged_in_user_can_update_book(self):
        self.client.login(username='testuser', password='testpass123')

        self.client.post(
            reverse('book_update', args=[self.book.id]),
            {
                'title': 'Advanced Django',
                'author': 'Astha'
            }
        )

        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Advanced Django')

    def test_logged_in_user_can_delete_book(self):
        self.client.login(username='testuser', password='testpass123')

        self.client.post(reverse('book_delete', args=[self.book.id]))

        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

# Create your tests here.
# test cases which tests all crud operations 