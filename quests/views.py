from django.shortcuts import render, redirect
from django.http import HttpResponse

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
    return render(request, 'create.html', {'form': form})


def list_view(request):
    return render(request, 'list.html', {'questboard_list': CreateQuestboard.objects.all()})


def edit_view(request, pk):
    obj = CreateQuestboard.objects.get(id=pk)
    form = CreateQuestboardForm(instance=obj)

    if request.method == "POST":
        form = CreateQuestboardForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list')

    return render(request, 'edit.html', {'form': form})


def add_view(request):
    if request.method == 'POST':
        form = AddQuestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            stars = form.cleaned_data['stars']
            obj = AddQuest.objects.create(
                name=name,
                description=description,
                stars=stars
            )
            obj.save()
            return redirect('card')

        render(request, "add.html", {'form': form})

    form = AddQuestForm()
    return render(request, 'add.html', {'form': form})


def card_view(request):
    return render(request, 'card.html', {'questcard_list': AddQuest.objects.all()})
