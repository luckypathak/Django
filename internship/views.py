from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {'categories': categories, 'products': products})

def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category = Category(categoryname=category_name)
        category.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def update_category(request, category_id):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        category = get_object_or_404(Category, pk=category_id)
        category.categoryname = new_name
        category.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        
        product = Product(product_name=product_name, price=price, quantity=quantity, description=description, categoryname=category)
        product.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
