from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
    categories = Category.objects.filter(parentid=None)
    data = {'categories': categories}
    return render(request,'pages/home.html', data)

def by_category(request, id):
    categories = Category.objects.filter(parentid=id)
    data = {'categories': categories}
    return render(request,'pages/home.html', data)