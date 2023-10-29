from django.db import models

class Emu(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  attitude = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
      return self.name
