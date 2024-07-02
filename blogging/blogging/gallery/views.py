from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
import requests

def product_list(request):
    products = Product.objects.all()
    return render(request, 'gallery/index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'gallery/detail.html', {'product': product})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'gallery/edit.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'gallery/delete.html', {'product': product})

# views.py

import requests
from django.shortcuts import render

def get_posts(request):
    # Make a GET request to the API URL
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)

    if response.status_code == 200:
        # If the request is successful, parse the JSON response
        posts = response.json()
        # Render the posts in a template
        return render(request, 'gallery/posts.html', {'posts': posts})
    else:
        # If there's an error, return an empty list
        posts = []
        return render(request, 'gallery/posts.html', {'posts': posts})

