
from django.contrib import admin
from book_manager.models import User, Book    #この部分を追加

admin.site.register(User)
admin.site.register(Book)