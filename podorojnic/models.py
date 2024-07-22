from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Direction(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.text


# class Best_co(models.Model):
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text


class Entry(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return f'{self.text[:50]}...'



class Country(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.text

class Info(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text[:50]}...'