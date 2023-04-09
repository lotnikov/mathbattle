from django.db import models

# Create your models here.

class Tournament(models.Model):

    Name = models.CharField(max_length=255)
    DateStart = models.DateField(verbose_name="Дата начала", blank=True)
    DateEnd = models.DateField(verbose_name="Дата окончания", blank=True)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=30)
    Logo = models.ImageField(upload_to='photo/tournaments/%Y/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name