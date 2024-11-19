from django import forms
from .models import Item, Group, Store


class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields= ['itemName', 'itemDescription', 'store', 'group', 'count', 'actualCount']
    

    itemName = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Enter Item Names'}))
    itemDescription = forms.CharField(widget=forms.Textarea(attrs={'class': 'inputs', 'placeholder': 'Enter Item Names'}))
    store = forms.ModelChoiceField(queryset=Store.objects.all(),  required=False, widget=forms.Select(attrs={'class': 'inputs', 'placeholder': 'Enter Item Quantity'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(),  required=True, widget=forms.Select(attrs={'class': 'inputs', 'placeholder': 'Enter Item Price'}))
    count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'inputs', 'placeholder': 'Enter Item Price'}))
    actualCount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'inputs', 'placeholder': 'Enter Item Price'}))



