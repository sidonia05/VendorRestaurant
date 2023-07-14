from _decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from cart.models import CartItem, Cart
from restaurantmenu.models import Product


def cart_id(request):
    cart_id_value = request.session.session_key
    if not cart_id_value:
        request.session.create()
        cart_id_value = request.session.session_key
    return cart_id_value


def add_cart(request, product_id):
    product = [Product.objects.get(id=product_id)]
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product[0], cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product[0],
            quantity=1,
            cart=cart
        )
        cart_item.save()

    # return HttpResponse(cart_item.product)
    # return HttpResponse(cart_item.quantity)
    return redirect('cart')
    # exit()


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)


    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return  redirect('cart')

def cart(request, total=0, quantity=0,tax=0, cart_items=None):
    grand_total = Decimal('0')
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
        tax = (Decimal('1.9') * total) / Decimal('100')
        tax = tax.quantize(Decimal('0.00'))  # Format the tax value with two decimal places
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'grand_total': grand_total,
        'tax': tax,
    }
    return render(request, 'cart/cart.html', context)


@login_required(login_url='login')
def checkout(request):
    total = 0
    quantity = 0
    cart_items = None
    grand_total = Decimal('0')
    tax = Decimal('0')

    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity

        tax = (Decimal('1.9') * total) / Decimal('100')
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'grand_total': grand_total,
        'tax': tax,
    }

    return render(request, 'cart/checkout.html', context)


