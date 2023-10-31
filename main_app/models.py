from django.db import models
from django.urls import reverse

class Emu(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  attitude = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
    return reverse('emu-detail', kwargs={'emu_id': self.id})