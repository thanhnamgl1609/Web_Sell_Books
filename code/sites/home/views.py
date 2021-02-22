from django.shortcuts import render
from .models import Category, Book
from django.db.models import Q

# Create your views here.
def index(request):
    categories = Category.objects.filter(parentid=None)
    products = Book.objects.filter(catid=8)

    products_list = [list(products[i * 2: i * 2 + 4]) for i in range(0,int(products.count() / 2))]
    if (len(products) >=4):
        last_item = products_list[len(products_list) - 1]
        last_item += list(products[0:4-len(last_item)])

    data = {'categories': categories, "products_list": products_list}
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

def search(request):
    query = request.GET.get('search')
    categories = Category.objects.filter(parentid=None)
    if query:
        results = Book.objects.filter(name__startswith=query)
    else:
        results=[]
    return render(request,'pages/by_category.html',{'categories': categories, 'products': results})