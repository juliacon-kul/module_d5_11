import datetime

from django.db import models

# Create your models here.

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    # authors = models.ManyToManyField(
    #     Author
    #     # through='Inspiration',
    #     # through_fields=('book', 'author'),
    # )
    author = models.ManyToManyField(Author)
    copy_count = models.SmallIntegerField(default= 1)
    price = models.DecimalField(max_digits = 10,decimal_places=2)

    def __str__(self):
        return self.title

class Friend(models.Model):
    full_name = models.TextField()
    books = models.ManyToManyField(Book,through='Abonement')

    def __str__(self):
        return self.full_name
class Abonement(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    date_taken = models.DateField()
    # date = models.DateTimeField(default = )

# class Inspiration(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     inspirer = models.ForeignKey(
#         Author,
#         on_delete=models.CASCADE,
#         related_name="inspired_works",
#     )
class Publisher(models.Model):
    full_name = models.TextField()
    city = models.TextField()
    country = models.CharField(max_length=2)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
#
    def __str__(self):
        return self.full_name


