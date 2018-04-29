from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from profiles.models import product
from profiles.models import Category
from .forms import ManageForm


def home(request, cat=0):
    template = 'home.html'

    if cat != 0:
        data = product.objects.filter(category=cat)
    else:
        data = product.objects.all()

    datacat = Category.objects.all()

    prod = {

        "product_number": data,
        "category_number": datacat
    }
    return render(request, template, prod)


def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)


def manage(request):
    if request.method == 'POST':
        form = ManageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ManageForm()

    return render(request, 'manage.html', {'form': form})


