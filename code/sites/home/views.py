from django.shortcuts import render
from .models import Category, Book

# Create your views here.
def index(request):
    categories = Category.objects.filter(parentid=None)
    data = {'categories': categories}
    return render(request,'pages/home.html', data)

def by_category(request, id):
    categories = Category.objects.filter(parentid=id)
    products = Book.objects.filter(catid=id)
    list_id = [category.id for category in categories]

    for uid in list_id:
        sub_categories = Category.objects.filter(parentid=uid)
        list_id += [category.id for category in sub_categories]
        products = products.union(Book.objects.filter(catid=uid))

    data = {'categories': categories, 'products': products}
    return render(request,'pages/by_category.html', data)