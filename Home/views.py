# views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Order, OrderItem
from django.http import HttpResponse

# Create your views here.
def index(request):
    order = Order.objects.first()  # Assuming you want the first order for demonstration
    total_quantity = order.calculate_total_quantity()
    return  render(request, "Home/index.html", {'total_quantity': total_quantity})



def product_list(request):
    products = Product.objects.all()
    order = Order.objects.first()  
    total_quantity = order.calculate_total_quantity()
    return render(request, 'Home/index.html', {'products': products, 'total_quantity': total_quantity})



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create()

    # Check if the product is already in the cart
    order_item, created = OrderItem.objects.get_or_create(product=product, order=order)

    # If the item is already in the cart, increment the quantity
    if not created:
        order_item.quantity += 1

    else:
        # If the item is not in the cart, set quantity to 1
        order_item.quantity = 1


    # Calculate and update the subtotal based on quantity and product price
    order_item.subtotal = order_item.quantity * product.price
    order_item.save()

    order.calculate_total_price()

    return redirect('product_list')

def cart(request):
    order = Order.objects.first()  # Assuming you want the first order for demonstration
    total_quantity = order.calculate_total_quantity()  # Calculate total quantity

    return render(request, 'Home/checkout.html', {'order': order, 'total_quantity': total_quantity})


def delete_from_cart(request, order_item_id):
    order_item = OrderItem.objects.get(id=order_item_id)
    order_item.delete()
    return redirect('cart')

def checkout(request):
    return render(request, 'Home/checkout.html')