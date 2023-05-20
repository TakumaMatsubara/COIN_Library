from django.urls import path
from . import views

app_name = "book_manager"

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
# ]


urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("", views.IndexView.as_view(), name="index"),
    path("add/", views.AddView.as_view(), name="add"),
    # path("add/", views.add, name="add"),
    path("return/<int:pk>/", views.ReturnView.as_view(), name="return"),
]