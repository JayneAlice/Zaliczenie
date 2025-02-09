from django.db import models

# Create your models here.
class Users(models.Model):

    name = models.CharField(max_length=100)
    username=models.CharField(max_length=16,unique=True,blank=True)
    email = models.EmailField(unique=True)
    bio= models.TextField(blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    order_number = models.IntegerField(primary_key=True,unique=True)

    def __int__(self):
        return self.order_number