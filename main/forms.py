from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["item_name", "item_price", "item_description"]
        
    def clean_itemName(self):
        item_name = self.cleaned_data["item_name"]
        return strip_tags(item_name)
    
    def clean_itemDescription(self):
        item_description = self.cleaned_data["item_description"]
        return strip_tags(item_description)

    def clean_item_price(self):
        item_price = self.cleaned_data["item_price"]
        return strip_tags(item_price)