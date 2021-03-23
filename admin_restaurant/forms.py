from django import forms
from main_restaurant.models import Category, Dish


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={'placeholder': 'Category name', 'required': 'required'})
                            )
    category_order = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'Category order in menu', 'required': 'required'
    }))
    category_photo = forms.ImageField(widget=forms.FileInput())
    is_visible = forms.BooleanField(initial=True, required=False)

    class Meta(object):
        model = Category
        fields = ('title', 'photo', 'category_order', 'is_visible')


class DishForm(forms.ModelForm):
    title = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={'placeholder': 'Dish name', 'required': 'required'})
                            )
    dish_photo = forms.ImageField(widget=forms.FileInput())
    dish_order = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'Dish order in menu', 'required': 'required'
    }))
    is_visible = forms.BooleanField(initial=True, required=False)
    price = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'dish price', 'required': "required"}))
    description = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Dish description', 'required': 'required'})
    )

    class Meta(object):
        model = Dish
        fields = ('title', 'dish_photo', 'dish_order', 'is_visible', 'price', 'description', 'category')
