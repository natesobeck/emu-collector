from django.shortcuts import render, redirect
from .models import Emu, BowTie
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def emu_index(request):
  emus = Emu.objects.all()
  return render(request, 'emus/index.html', { 'emus': emus })

def emu_detail(request, emu_id):
  emu = Emu.objects.get(id=emu_id)
  feeding_form = FeedingForm()
  return render(request, 'emus/detail.html', { 'emu': emu, 'feeding_form': feeding_form })

class EmuCreate(CreateView):
  model = Emu
  fields = '__all__'

class EmuUpdate(UpdateView):
  model = Emu
  fields = ['age', 'attitude', 'description']

class EmuDelete(DeleteView):
  model = Emu
  success_url = '/emus/'

class BowTieCreate(CreateView):
  model = BowTie
  fields = '__all__'

def add_feeding(request, emu_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.emu_id = emu_id
    new_feeding.save()
  return redirect('emu-detail', emu_id=emu_id)