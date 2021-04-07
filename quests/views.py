from django.shortcuts import render, redirect

from .forms import *
from .models import *

def index(request):
    return redirect('home')


def home_view(request):
    return render(request, 'home.html')


def create_view(request):
    if request.method == 'POST':
        form = CreateQuestboardForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            stars = form.cleaned_data['stars']
            obj = CreateQuestboard.objects.create(
                name=name,
                description=description,
                stars=stars
            )
            obj.save()
            return redirect('list')

        render(request, "create.html", {'form': form})

    form = CreateQuestboardForm()
    return render(request, "create.html", {'form': form})


def list_view(request):
    return redirect('home')
