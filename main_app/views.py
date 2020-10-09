from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Character, Weapon
from .forms import LevelingForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def characters_index(request):
    characters = Character.objects.filter(user=request.user)
    return render(request, 'characters/index.html', {'characters': characters})


@login_required
def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    weapons_character_doesnt_have = Weapon.objects.exclude(
        id__in=character.weapons.all().values_list('id'))
    leveling_form = LevelingForm
    return render(request, 'characters/detail.html', {'character': character, 'leveling_form': leveling_form, 'weapons': weapons_character_doesnt_have})


@login_required
def add_leveling(request, character_id):
    form = LevelingForm(request.POST)
    if form.is_valid():
        new_leveling = form.save(commit=False)
        new_leveling.character_id = character_id
        new_leveling.save()
    return redirect('detail', character_id=character_id)


@login_required
def assoc_weapon(request, character_id, weapon_id):
    Character.objects.get(id=character_id).weapons.add(weapon_id)
    return redirect('detail', character_id=character_id)


class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    fields = ['name', 'gender', 'description', 'element']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    fields = ['description', 'element']


class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = '/characters/'


class WeaponList(LoginRequiredMixin, ListView):
    model = Weapon


class WeaponDetail(LoginRequiredMixin, DetailView):
    model = Weapon


class WeaponCreate(LoginRequiredMixin, CreateView):
    model = Weapon
    fields = '__all__'


class WeaponUpdate(LoginRequiredMixin, UpdateView):
    model = Weapon
    fields = ['name', 'type']


class WeaponDelete(LoginRequiredMixin, DeleteView):
    model = Weapon
    success_url = '/weapons/'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
