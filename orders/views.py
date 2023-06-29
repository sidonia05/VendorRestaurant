from django.shortcuts import render
from django.http import HttpResponse

# Global variable for the order number
order_counter = 1

def place_order(request):
    global order_counter

    if request.method == 'POST':
        payment_type = request.POST.get('payment_type')

        # Increment the order number
        order_number = order_counter
        order_counter += 1

        # Process the data and perform the corresponding actions

        # Display the confirmation message
        message = f"The order has been successfully placed. Payment type: {payment_type}, Order number: {order_number}"
        return HttpResponse(message)

    return render(request, 'order/place-order.html')
