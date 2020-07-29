from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
import requests
from cart.forms import CartAddProductForm

from .forms import *
from .models import *

pix_url = "https://pixabay.com/api/?key=17560993-1dca8c47b9291ed16f15f4a9b&q=impressions&image_type=paintings"


def product_list(request, category_slug=None):
    category = None
    painting_url = generate_pictures(category_slug)
    photo_data = requests.get(painting_url).json()
    photo_display = []
    photo_description = []
    for dic in photo_data["hits"]:
        for key in dic:
            if key == "webformatURL":
                photo_display.append(dic[key])
            if key == "tags":
                photo_description.append(dic[key])

    categories = Category.objects.all()

    products = Product.objects.filter(available=True)

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
    photo_display = photo_display[:len(products)]
    photo_description = photo_description[:len(products)]

    context = {
        "category": category,
        "categories": categories,
        "products": products,
        "photo_display": photo_display,
        'photo_description': photo_description

    }
    return render(request, "shop/product/list.html", context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    product = get_object_or_404(Product, id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def generate_pictures(category_slug):
    photo_url = f"https://pixabay.com/api/?key=17560993-1dca8c47b9291ed16f15f4a9b&q={category_slug}&image_type=photo"
    return photo_url


def about_us(request):
    map_url = "https://www.google.com/maps/embed/v1/place?key=AIzaSyCpzrShdNi9RlzJ6W5PEvLxHsWmBip-sPsw&q=9126+Keating+Ave,+Skokie,+IL+60076"
    return render(request, "shop/product/about_us.html", {map_url: "map_url"})

class CreateAccount(CreateView):
    form_class = CreateAccountForm
    success_url = reverse_lazy('base:home')
    template_name = 'registration/create_account.html'

    def form_valid(self, form):
        view = super(CreateAccount, self).form_valid(form)
        username, password = form.cleaned_data.get(
                'username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
