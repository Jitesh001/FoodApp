from pickle import NONE
from webbrowser import get
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Item
from .form import ItemForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
# def index(request):
#     item_list = Item.objects.all()
#     context = {'items': item_list}
#     return render( request,'food/index.html', context) 

class indexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'     #'items' is name used in index.html file

# def details(request, itm_id):
#     item = Item.objects.get(id=itm_id)
#     context = {'item' :  item}
#     return render(request, 'food/details.html', context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/details.html'
    #instend of using context variable we directly used 'object' as a variaale in details.html    

# def add_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food:index') #index is view function name check urls.py
#     return render(request, 'food/item-form.html', {'form':form})

class AddItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request, itm_id):
    item = Item.objects.get(id=itm_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form, 'item':item})

def delete_item(request, itm_id):
    item = Item.objects.get(id=itm_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item':item})