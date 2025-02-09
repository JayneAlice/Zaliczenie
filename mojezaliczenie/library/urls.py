from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("", views.welcome_view),
    path("authors",views.author_list),
    path("books",views.book_list),
    path("users",views.user_list),
    path("categorys",views.category_list),
    path("orders",views.order_list),
]