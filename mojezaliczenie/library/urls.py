from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("", views.welcome_view),
    path("authors",views.author_list),
    path("authors/<str:name>", views.author_detail),
    path("books",views.book_list),
    path("books/<str:title>", views.book_detail),
    path("users",views.user_list),
    path("users/<str:name>", views.user_detail),
    path("categorys",views.category_list),
    path("categories/<str:name>", views.category_detail),
    path("orders",views.order_list),
    path("orders/<int:id>", views.order_detail),
]