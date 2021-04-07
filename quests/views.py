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
        form = QuestboardForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            stars = form.cleaned_data['stars']
            obj = Questboard.objects.create(
                name=name,
                description=description,
                stars=stars
            )
            obj.save()
            return redirect('card')

        render(request, "create.html", {'form': form})

    form = QuestboardForm()
    return render(request, 'create.html', {'form': form})


def list_view(request):
    return render(request, 'list.html', {'questboard_list': Questboard.objects.all()})


def edit_view(request, pk):
    obj = Questboard.objects.get(id=pk)
    form = QuestboardForm(instance=obj)

    if request.method == "POST":
        form = QuestboardForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list')

    return render(request, 'edit.html', {'form': form})


def add_view(request, pk):
    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            stars = form.cleaned_data['stars']
            obj = Quest.objects.create(
                name=name,
                description=description,
                stars=stars
            )
            obj.save()
            return redirect('card')

        render(request, "add.html", {'form': form})

    form = QuestForm()
    return render(request, 'add.html', {'form': form})


def board_view(request, pk):
    course = Questboard.objects.get(pk=pk)
    return render(request, 'board.html', {'quest_list': Quest.objects.filter(board=course), 'course': course})
