from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Komment(models.Model):
    koment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.koment



class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    komment = models.ManyToManyField(Komment)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
