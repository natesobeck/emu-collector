from django.shortcuts import render
from .models import Emu

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