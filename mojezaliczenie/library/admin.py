from django.contrib import admin
from .models import Order,Author,Book,Users,Category

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Users)
admin.site.register(Order)