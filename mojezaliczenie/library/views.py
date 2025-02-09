from django.shortcuts import render, get_object_or_404,redirect
# Create your views here.
# kod umieszczamy w pliku views.py wybranej aplikacji

from django.http import HttpResponse
import datetime
from .models import Author,Book,Users,Category,Order

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        home page
        </body></html>"""
    return HttpResponse(html)

def book_list(request, id):
    books = Book.objects.all()
    return render(request,
                'library/books/list.html', 
                  {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request,
                'library/authors/list.html', 
                  {'authors': authors})

def user_list(request):
    users = Users.objects.all()
    return render(request,
                'library/users/list.html', 
                  {'users': users})

def category_list(request):
    categories = Category.objects.all()
    return render(request,
                'library/categories/list.html', 
                  {'categories': categories})

def order_list(request):
    orders = Order.objects.all()
    return render(request,
                'library/orders/list.html', 
                  {'orders': orders})