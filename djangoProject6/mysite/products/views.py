from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from . import forms
from .models import Product


# Create your views here.
def add_products(request):
    if request.method == "GET":
        form = forms.ProductForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse('Add Successfully!')
    else:
        form = forms.ProductForm()
    return render(request, 'forms.html', context={'form': form, })


def update_products(request, p_id):
    p = Product.objects.get(pk=p_id)
    if request.method == "GET":
        form = forms.ProductForm(request.GET or None, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponse('Update Successfully!')
    else:
        form = forms.ProductForm(instance=p)
    return render(request, 'forms.html', context={'form': form, })


def delete_products(request, p_id):
    Product.objects.get(pk=p_id).delete()
    return HttpResponse('Deleted Successfully!')

# Create your views here.
