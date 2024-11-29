from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))
    tags = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Product
        fields = ["name", "icon", "tagline", "description", "tags", "website"]

    def save(self, commit=True):
        product = super().save(commit=False)
        tags_string = self.cleaned_data["tags"]
        tags_list = [tag.strip() for tag in tags_string.split(",") if tag.strip()]
        product.tags = tags_list
        if commit:
            product.save()
        return product
