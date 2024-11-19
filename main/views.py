from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, RedirectView, DetailView, CreateView
from .models import Item, Group, Store
from .forms import ItemForm


# Create your views here.

# class MainView(ListView):
    
#     template_name = 'home.html'
    
#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         items = Item.objects.all()
#         context['items'] = items
#         return context
    
def main(request):
    items = Item.objects.all()
    context  = {
        'items': items,
    }
    return render(request, 'home.html', context=context)
    

    
class ItemDetailView(DetailView):
    template_name = 'item_detail.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Item.objects.filter(pk=self.kwargs['pk'])
    

def updatingform(request, id):
    # Get the specific item by its primary key (pk)
    item = get_object_or_404(Item, pk=id)
    
    # Bind the form with the item's current data or the submitted data
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()  # Save the updated instance
            return redirect('main')  # Redirect to a detail view or list view
            # return redirect('item_detail', pk=item.pk)  # Redirect to a detail view or list view
    else:
        form = ItemForm(instance=item)  # Pre-fill the form with the item's data
    return render(request, 'updatingform.html', {'form': form})
    
    
def newitem(request):
    form = ItemForm(request.POST)
    return render(request, 'itemform.html', {'form': form})


def additem(request):
    form = ItemForm(request.POST, use_required_attribute=False)
    group = Group.objects.get(pk=1)
    store = Store.objects.get(pk=1)
    if request.method == 'POST':
        item = Item(itemName=request.POST['itemName'], group=group, store=store, count=request.POST['count'], actualCount=request.POST['actualCount'])
        item.save()
        return redirect('main')
    else:
        return render(request, 'itemform.html', {'form': form})
    
    
