from django.test import TestCase
from users.models import User
from books.models import Book
from round_table.models import Forum, Replies

class ForumModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        book = Book.objects.create(title='Test Book', author='Test Author')
        Forum.objects.create(author=user, book=book, title='Test Title', content='Test Content')

    def test_author_label(self):
        forum = Forum.objects.get(id=1)
        field_label = forum._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_title_max_length(self):
        forum = Forum.objects.get(id=1)
        max_length = forum._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_content_max_length(self):
        forum = Forum.objects.get(id=1)
        max_length = forum._meta.get_field('content').max_length
        self.assertEquals(max_length, 5000)

class RepliesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        book = Book.objects.create(title='Test Book', author='Test Author')
        forum = Forum.objects.create(author=user, book=book, title='Test Title', content='Test Content')
        Replies.objects.create(author=user, parent_forum=forum, content='Test Reply Content')

    def test_author_label(self):
        reply = Replies.objects.get(id=1)
        field_label = reply._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_content_max_length(self):
        reply = Replies.objects.get(id=1)
        max_length = reply._meta.get_field('content').max_length
        self.assertEquals(max_length, 5000)
