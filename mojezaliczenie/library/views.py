from urllib import request
from django.shortcuts import get_object_or_404, render,redirect
# Create your views here.
# kod umieszczamy w pliku views.py wybranej aplikacji

from django.http import HttpResponse,Http404
import datetime

from .forms import OrderForm
from .models import Author,Book,Users,Category,Order

def welcome_view(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_orders = Order.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_orders': num_orders,
    }
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Our Library!</title>
    </head>
    <body>
        <h1>Welcome to Our Library!</h1>

        <p>Number of Books: {num_books}</p>
        <p>Number of Authors: {num_authors}</p>
        <p>Number of Orders: {num_orders}</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def book_list(request):
    books = Book.objects.all()
    return render(request,
                'library/books/list.html', 
                  {'books': books})

def book_detail(request, title):
    book = Book.objects.get(title=title)

    return render(request,
                'library/books/detail.html', 
                  {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request,
                'library/authors/list.html', 
                  {'authors': authors})

def author_detail(request, name):
    author = Author.objects.get(name=name)

    return render(request,
                'library/authors/detail.html', 
                  {'author': author})

def author_books(request, name):
    author = get_object_or_404(Author, name=name)

    books_by_author = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books': books_by_author,
    }

    return render(request, 'library/authors/book.html', context)

def user_list(request):
    users = Users.objects.all()
    return render(request,
                'library/users/list.html', 
                  {'users': users})

def user_detail(request, name):
    user = Users.objects.get(name=name)

    return render(request,
                'library/users/detail.html', 
                  {'user': user})

def category_list(request):
    categories = Category.objects.all()
    return render(request,
                'library/categories/list.html', 
                  {'categories': categories})

def category_detail(request, name):
    category = Category.objects.get(name=name)

    return render(request,
                'library/categories/detail.html', 
                  {'category': category})

def order_list(request):
    orders = Order.objects.all()
    return render(request,
                'library/orders/list.html', 
                  {'orders': orders})

def order_detail(request, order_number):
    order = Order.objects.get(order_number = order_number)

    return render(request,
                'library/orders/detail.html', 
                  {'order': order})

def order_create(request):
    if request.method == 'POST':
     form = OrderForm(request.POST)
     if form.is_valid():
        order=form.save()
        return redirect('order_detail',order.order_number)
    else:
      form = OrderForm()

    return render(request,
                'library/orders/create.html',
                {'form': form})

def order_update(request,order_number):
    try:
        order = Order.objects.get(order_number=order_number)
    except Order.DoesNotExist:
        raise Http404("Order with that id doesn't exist")
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
          order=form.save()
          return redirect('order_detail', order_number)
    else:
      form = OrderForm()

    return render(request,
                'library/orders/update.html',
                {'form': form})

def order_delete(request,order_number):
    try:
       order = Order.objects.get(order_number=order_number)
    except Order.DoesNotExist:
        raise Http404("Order with that id doesn't exist") 
        
    if request.method == "POST":
      form = OrderForm(request.POST)
      if form.is_valid():
        order.delete()
    return redirect('order_list')
    
    return render(request,
              'library/orders/delete.html',
              {'form': form})