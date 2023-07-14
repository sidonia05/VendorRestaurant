from django.shortcuts import render
from django.http import HttpResponse

# Global variable for the order number
from orders.models import Order


def place_order(request):
    order_counter = 1

    if request.method == 'POST':
        payment_type = request.POST.get('payment_type')

        # Increment the order number
        order = Order.objects.filter().last()
        if order is not None:
            order.number += order_counter
        else:
            order = Order(number=order_counter, user=request.user)

        order.save()
        order_counter += 1

        # Process the data and perform the corresponding actions

        # Display the confirmation message
        message = f"The order has been successfully placed. Payment type: {payment_type}, Order number: {order.number}"
        return HttpResponse(message)

    return render(request, 'order/place-order.html')
