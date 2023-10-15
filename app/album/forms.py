from django import forms

class CategoryForm(forms.Form):
    slug = forms.CharField(required=False)
