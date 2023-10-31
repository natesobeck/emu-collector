from django.shortcuts import render
from .models import Emu
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
  return render(request, 'emus/detail.html', { 'emu': emu })

class EmuCreate(CreateView):
  model = Emu
  fields = '__all__'

class EmuUpdate(UpdateView):
  model = Emu
  fields = ['age', 'attitude', 'description']

class EmuDelete(DeleteView):
  model = Emu
  success_url = '/emus/'