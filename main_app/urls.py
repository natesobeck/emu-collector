from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('emus/', views.emu_index, name='emu-index'),
  path('emus/<int:emu_id>/', views.emu_detail, name='emu-detail'),
  path('emus/create/', views.EmuCreate.as_view(), name='emu-create')
]