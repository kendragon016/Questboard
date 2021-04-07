from django.shortcuts import render, redirect
from django.http import HttpRequest

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

            go_to = '/board/teacher/' + str(obj.pk)
            return redirect(go_to)

        render(request, "create.html", {'form': form})

    form = QuestboardForm()
    return render(request, 'create.html', {'form': form})


def list_view(request):
    boards = Questboard.objects.all().order_by('pk')
    return render(request, 'list.html', {'questboard_list': boards})


def edit_board(request, pk):
    obj = Questboard.objects.get(id=pk)
    form = QuestboardForm(instance=obj)

    if request.method == "POST":
        form = QuestboardForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()

            go_to = '/board/teacher/' + str(pk)
            return redirect(go_to)

    return render(request, 'edit.html', {'form': form})


def edit_quest(request, pk):
    obj = Quest.objects.get(id=pk)
    form = QuestForm(instance=obj)

    if request.method == "POST":
        form = QuestForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()

            go_to = '/board/teacher/' + str(obj.board.pk)
            return redirect(go_to)

    return render(request, 'edit.html', {'form': form})


def add_view(request, pk):
    course = Questboard.objects.get(pk=pk)

    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            stars = form.cleaned_data['stars']
            everyone = form.cleaned_data['everyone']
            obj = Quest.objects.create(
                board=course,
                name=name,
                description=description,
                stars=stars,
                everyone=everyone,
            )
            obj.save()

            go_to = '/board/teacher/' + str(pk)
            return redirect(go_to)

    form = QuestForm()
    return render(request, 'add.html', {'form': form, 'course': course})


def board_view(request, str, pk):
    course = Questboard.objects.get(pk=pk)
    cards = Quest.objects.filter(board=course).order_by('pk')
    form = SignUpForm()
    return render(
        request,
        'board.html',
        {'quest_list': cards,
         'course': course,
         'form': form
         }
        )


def confirm_dibs(request, str, pk):
    obj = Quest.objects.get(pk=pk)
    dibs_list = []
    if obj.sign_ups:
        for i in obj.sign_ups:
            dibs_list.append(i)
    dibs_list.append(str)

    obj.sign_ups = dibs_list
    obj.save()

    go_to ='/board/student/' + "% s" % obj.board.pk
    return redirect(go_to)



def sign_up(request, pk):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            obj = Quest.objects.get(pk=pk)

            return render(request, 'confirm.html', {'name': name, 'quest':obj})
