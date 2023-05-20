
from django.contrib import admin
from book_manager.models import UserList, BookList    #この部分を追加

admin.site.register(UserList)
admin.site.register(BookList)