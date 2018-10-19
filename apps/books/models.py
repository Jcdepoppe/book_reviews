from django.db import models
from apps.log_reg.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="book")
    user = models.ForeignKey(User, related_name="book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    book = models.ForeignKey(Book, related_name="b_reviews")
    user = models.ForeignKey(User, related_name="u_reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)