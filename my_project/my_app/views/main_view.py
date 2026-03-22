from django.shortcuts import render,redirect,get_object_or_404
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


# edit method 
def edit_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        description = request.POST.get('description')

        product.title = title
        product.category = category
        product.price = price
        product.description = description
        product.save()
        return redirect('index')


    return render(request,'main/edit_product.html',{'prev_data':product})



# for deleting the product
def delete_product(request, id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id) 
    product.delete()
    return redirect('index')






def about_method(request):
    return render(request,'main/about.html')




