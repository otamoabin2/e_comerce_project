from django.urls import path
from . import views
app_name = 'payment'
urlpatterns = [
    # path('payment/', views.payment, name='payment'),
    path('processing/', views.payment_processing, name='processing'),
    path('complete/<str:args>/', views.payment_complete, name='complete'),
  
]
