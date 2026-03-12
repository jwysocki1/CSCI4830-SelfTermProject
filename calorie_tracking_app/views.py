from django.shortcuts import render
from .models import Date
from .forms import DateForm, MealForm

# Create your views here.

def index(request):
    dates = Date.objects.all()

    if request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DateForm()

    return render(request, 'index.html')


