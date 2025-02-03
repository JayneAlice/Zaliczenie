from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
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

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', 
                  {'books': books})

# def book_detail(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     return render(request, 'book_detail.html', 
#                   {'book': book})

# def edit_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == "POST":
#         # Logika aktualizacji książki
#         pass
#     return render(request, 'edit_book.html', 
#                   {'book': book})

# def delete_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == "POST":
#         book.delete()
#         return redirect('book_list')
#     return render(request, 'delete_book.html', 
#                   {'book': book})

# def orders_summary(request):
#     # Logika do zestawienia zamówień
#     orders = Order.objects.all()  # Można filtrować według daty
#     return render(request, 'orders_summary.html', 
#                   {'orders': orders})

# def books_by_category(request, category_id):
#     books = Book.objects.filter(category_id=category_id)
#     return render(request, 'books_by_category.html', 
#                   {'books': books})