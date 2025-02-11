from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("", views.welcome_view,name='home'),
    path("authors",views.author_list,name='author_list'),
    path("authors/<str:name>", views.author_detail,name='author_detail'),
    path("authors/<str:title>",views.author_books,name='author_books'),
    path("books",views.book_list,name='book_list'),
    path("books/<str:title>", views.book_detail,name='book_detail'),
    path("users",views.user_list,name='user_list'),
    path("users/<str:username>", views.user_detail,name='user_detail'),
    path("categorys",views.category_list,name='category_list'),
    path("categories/<str:name>", views.category_detail,name='category_detail'),
    path("orders",views.order_list,name='order_list'),
    path("orders/<int:order_number>", views.order_detail,name='order_detail'),
    path("orders/add", views.order_create,name='order_create'),
    path("orders/<int:order_number>/change", views.order_update,name='order_update'),
    path("orders/<int:order_number>/delete", views.order_delete,name='order_delete'),
]