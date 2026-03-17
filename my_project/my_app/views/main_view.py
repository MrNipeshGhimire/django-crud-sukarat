from django.shortcuts import render,redirect
from ..models import Product

def index_method(request):
    product =  Product.objects.all()
    return render(request,'main/index.html',{'data':product})


def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')

        product = Product.objects.create(
            title=title,
            category=category,
            price = price,
            description = description
        )
        product.save()
        return redirect('index')

    return render(request,'main/add_product.html')

def edit_product(request):
    return render(request,'main/edit_product.html')


def about_method(request):
    return render(request,'main/about.html')


