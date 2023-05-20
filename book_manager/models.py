from django.db import models
from datetime import date

# Create your models here.
class UserList(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.CharField('学籍番号', max_length=5)
    username = models.CharField('ユーザー名', max_length=100)

    def __str__(self):
        return self.studentid


class BookList(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(UserList, on_delete=models.CASCADE)
    author = models.CharField('著者', max_length=50)
    title = models.CharField('本のタイトル', max_length=200)
    date = models.DateField('貸出日', default = date.today())

    def __str__(self):
        return self.title
