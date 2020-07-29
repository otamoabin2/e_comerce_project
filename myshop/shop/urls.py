from django.urls import path
from . import views
from .views import *



app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('about/', views.about_us, name='about_us'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('create-account/', CreateAccount.as_view(), name="create_account"),

]

