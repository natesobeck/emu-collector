from django.shortcuts import render

# Create your views here.
class Emu:
  def __init__(self, name, age, description, attitude):
    self.name = name
    self.age = age
    self.description = description
    self.attitude = attitude

emus = [
  Emu('Fred', 15, 'Total bro', 'Chill'),
  Emu('Barry', 4, 'Loves to mess with you', 'Mischievious'),
  Emu('Sally', 6, 'She is sweet when she opens up', 'Shy')
]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def emu_index(request):
  return render(request, 'emus/index.html', { 'emus': emus })