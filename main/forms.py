from django.forms import ModelForm, TextInput, NumberInput, Select 
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model=Item
        fields='__all__'
    
    widgets ={
        'itemName' : TextInput(attrs={'class': 'inputs', 'placeholder': 'Enter Item Names'}),
        'itemDescription' : TextInput(attrs={'class': 'inputs', 'placeholder': 'Enter Item Description'}),
        'store' : NumberInput(attrs={'class': 'inputs', 'placeholder': 'Enter Item Quantity'}),
        'group' : NumberInput(attrs={'class': 'inputs', 'placeholder': 'Enter Item Price'}),
        'count' : Select(attrs={'class': 'form-control'}),
    }
    
#     itemName
# itemDescription
# store
# group
# count
# actualCount