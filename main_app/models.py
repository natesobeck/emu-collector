from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class BowTie(models.Model):
  color = models.CharField(max_length=20)
  cost = models.IntegerField()

  def __str__(self):
    return self.color
  
  def get_absolute_url(self):
    return reverse('bowtie-detail', kwargs={'pk': self.id})

class Emu(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  attitude = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  bowties = models.ManyToManyField(BowTie)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
    return reverse('emu-detail', kwargs={'emu_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
  
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  emu = models.ForeignKey(Emu, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']