from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import *

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
            order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            
            cart.clear()
            
            # launch asynchronous task
            # order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:processing'))
          
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/create.html',{'cart': cart, 'form': form})
  
    


