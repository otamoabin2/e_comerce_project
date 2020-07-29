from django.urls import reverse 
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from django.http import JsonResponse
import stripe
stripe.api_key = "sk_test_51H9cgtE3k5W9WHe6l75Yy8HO9KTEiXFDi0ZvTBKelYathCTXJM9yet7vuMWRFAjDbmXStUKExsVzdR6cTRv0jO9O00aBW5iFvN"




def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    
    
    return render (request,'payment/process' , {'total_cost': total_cost})

def payment_processing(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    
    # if successful:
    #         order.paid = True
    #         order.braintree_id = result.transaction.id
    #         order.save()
    #         payment_completed.delay(order.id)
    
    return redirect (reverse('payment:complete', args=[total_cost]))



 
def payment_complete(request, args):
    amount = args
    
    return render(request,'payment/complete', {'amount': amount})