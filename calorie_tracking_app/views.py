from django.shortcuts import render, redirect
from .models import Date, Meal
from .forms import DateForm, MealForm

# Create your views here.

def index(request):
    dates = Date.objects.all()

    if request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DateForm()

    return render(request, 'index.html', {'form' : form, 'dates' : dates})

def delete_date(request, date):
    date_to_delete = Date.objects.get(date=date)
    date_to_delete.delete()

    return index(request)

def manage_meals(request, date):
    meals_to_manage = Date.objects.filter(date=date)

    if request.method == "POST":
        form= MealForm()
    else:
        form = MealForm()

    return render(request, 'meals.html', {'form' : form, 'meals' : meals_to_manage, 'date' : date})

def edit_meal(request, name):
    return render(request, 'meals.html')

def delete_meal(request, name):
    return render(request, 'meals.html')