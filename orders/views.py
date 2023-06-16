from django.shortcuts import render
from django.http import HttpResponse

# Variabila globală pentru numărul comenzii
order_counter = 1

def place_order(request):
    global order_counter

    if request.method == 'POST':
        payment_type = request.POST.get('payment_type')

        # Incrementează numărul comenzii
        order_number = order_counter
        order_counter += 1

        # Procesează datele și efectuează acțiunile corespunzătoare

        # Afișează mesajul de confirmare
        message = f"Comanda a fost plasată cu succes. Tipul de plată: {payment_type}, Numărul comenzii: {order_number}"
        return HttpResponse(message)

    return render(request, 'order/place-order.html')
