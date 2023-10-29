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