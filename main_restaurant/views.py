from django.shortcuts import render, redirect
from .models import *
from main_restaurant.forms import FormMessage


# Create your views here.
def main_page_view(request):

    if request.method == 'POST':
        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for items in categories:
        dishes = Dish.objects.filter(category=items.pk).filter(is_visible=True).order_by('dish_order')
        items.dishes = dishes

    specials = Dish.objects.filter(category__title='Specials')
    team = Team.objects.all().filter(is_visible=True)
    story = Story.objects.all().filter(is_visible=True)
    rest_info = RestInfo.objects.all()
    form = FormMessage()

    return render(request, "index.html", context={
        "categories": categories,
        'specials': specials,
        "team": team[0],
        "story": story[0],
        "rest_info": rest_info,
        "form": form

    })


def dish_page_view(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, "dish_info.html", context={'dish': dish})
