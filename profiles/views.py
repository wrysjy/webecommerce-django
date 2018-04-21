from django.shortcuts import render

# Create your views here.
from profiles.models import product


def home(request):
    #context = locals()
    template = 'home.html'
    data = product.objects.all()
    prod = {
        "product_number": data
    }
    return render(request, template, prod)


def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)

