from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.CharField('学籍番号', max_length=5)
    username = models.CharField('ユーザー名', max_length=100)

    def __str__(self):
        return self.studentid


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="学籍番号")
    author = models.CharField(max_length=50, verbose_name="著者")
    title = models.CharField(max_length=200, verbose_name="タイトル")
    date = models.DateField(default = date.today(), verbose_name="貸出日")

    def __str__(self):
        return self.title
