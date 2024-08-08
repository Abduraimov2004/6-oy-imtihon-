from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    text = models.TextField()


    def __str__(self):
        return f'{self.author} - {self.date_add}'
