from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid
from django.db import models
from datetime import date



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('event:event_list_by_category', args=[self.slug])


class Judge(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    country = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering=('name','country')
        verbose_name='judge'
        verbose_name_plural='judges'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('event:event_list_by_judge', args=[self.slug])


class Club(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    country = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering=('name','country')
        verbose_name='kennel_club'
        verbose_name_plural='kennel_clubs'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('event:event_list_by_club', args=[self.slug])

class Dog(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering=['name']
        verbose_name='dog'
        verbose_name_plural='dogs'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('event:event_list_by_dog', args=[self.slug])




class Dog_Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'dog_events')
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE, related_name = 'judges')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = 'clubs')
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name = 'Ράτσες_Σκύλων')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='events/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2)
    date = models.DateTimeField(blank=True, null=True)


    class Meta:
        ordering = ('-date',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('event:event_detail', args=[self.id, self.slug])





