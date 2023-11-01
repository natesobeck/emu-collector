from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('emus/', views.emu_index, name='emu-index'),
  path('emus/<int:emu_id>/', views.emu_detail, name='emu-detail'),
  path('emus/create/', views.EmuCreate.as_view(), name='emu-create'),
  path('emus/<int:pk>/update/', views.EmuUpdate.as_view(), name='emu-update'),
  path('emus/<int:pk>/delete/', views.EmuDelete.as_view(), name='emu-delete'),
  path('emus/<int:emu_id>/add-feeding', views.add_feeding, name='add-feeding'),
  path('bowties/create/', views.BowTieCreate.as_view(), name='bowtie-create'),
  path('bowties/<int:pk>/', views.BowTieDetail.as_view(), name='bowtie-detail'),
  path('bowties/', views.BowTieList.as_view(), name='bowtie-index'),
  path('bowties/<int:pk>/update/', views.BowTieUpdate.as_view(), name='bowtie-update'),
  path('bowties/<int:pk>/delete/', views.BowTieDelete.as_view(), name='bowtie-delete'),
  path('emus/<int:emu_id>/assoc-bowtie/<int:bowtie_id>/', views.assoc_bowtie, name='assoc-bowtie'),
  path('accounts/signup/', views.signup, name='signup'),
]