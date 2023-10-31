from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Emu(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  attitude = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
    return reverse('emu-detail', kwargs={'emu_id': self.id})
  
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

