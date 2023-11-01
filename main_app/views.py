from django.shortcuts import render, redirect
from .models import Emu, BowTie
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def emu_index(request):
  emus = Emu.objects.filter(user=request.user)
  return render(request, 'emus/index.html', { 'emus': emus })

@login_required
def emu_detail(request, emu_id):
  emu = Emu.objects.get(id=emu_id)
  unassigned_bowties = BowTie.objects.exclude(id__in = emu.bowties.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'emus/detail.html', { 'emu': emu, 'feeding_form': feeding_form, 'bowties': unassigned_bowties })

class EmuCreate(LoginRequiredMixin, CreateView):
  model = Emu
  fields = ['name', 'age', 'attitude', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class EmuUpdate(LoginRequiredMixin, UpdateView):
  model = Emu
  fields = ['age', 'attitude', 'description']

class EmuDelete(LoginRequiredMixin, DeleteView):
  model = Emu
  success_url = '/emus/'

class BowTieCreate(LoginRequiredMixin, CreateView):
  model = BowTie
  fields = '__all__'

class BowTieList(LoginRequiredMixin, ListView):
  model = BowTie

class BowTieDetail(LoginRequiredMixin, DetailView):
  model = BowTie

class BowTieUpdate(LoginRequiredMixin, UpdateView):
  model = BowTie
  fields = ['color', 'cost']

class BowTieDelete(LoginRequiredMixin, DeleteView):
  model = BowTie
  success_url = '/bowties/'

@login_required
def add_feeding(request, emu_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.emu_id = emu_id
    new_feeding.save()
  return redirect('emu-detail', emu_id=emu_id)

@login_required
def assoc_bowtie(request, emu_id, bowtie_id):
  Emu.objects.get(id=emu_id).bowties.add(bowtie_id)
  return redirect('emu-detail', emu_id=emu_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('emu-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)