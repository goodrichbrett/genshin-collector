from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character
from .forms import LevelingForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})


def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    leveling_form = LevelingForm
    return render(request, 'characters/detail.html', {'character': character, 'leveling_form': leveling_form})


def add_leveling(request, character_id):
    form = LevelingForm(request.POST)
    if form.is_valid():
        new_leveling = form.save(commit=False)
        new_leveling.character_id = character_id
        new_leveling.save()
    return redirect('detail', character_id=character_id)


class CharacterCreate(CreateView):
    model = Character
    fields = '__all__'


class CharacterUpdate(UpdateView):
    model = Character
    fields = ['description', 'element']


class CharacterDelete(DeleteView):
    model = Character
    success_url = '/characters/'
