from django.db import models

# Create your models here.

class Physics(models.Model):
  physics = models.CharField(
    max_length=64,
    blank=False,
  )
  def __str__(self):
    return self.physics

class Device(models.Model):
  device = models.CharField(
    max_length=64,
    blank=False,
  )
  def __str__(self):
    return self.device

class Place(models.Model):
  place = models.CharField(
    max_length=64,
    blank=False,
  )
  def __str__(self):
    return self.place

class Log(models.Model):
  created_at = models.DateTimeField(
    verbose_name='登録時間',
    auto_now_add=True,
  )
  value = models.FloatField(
    verbose_name='値',
    blank=True,
  )
  physics = models.ForeignKey(Physics, on_delete=models.CASCADE, related_name='log_physics')
  device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='log_device')
  place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='log_place')

  def __str__(self):
    return str(self.created_at)
  
  class Meta:
    verbose_name = '採取データ'
    verbose_name_plural = '採取データ'

