from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
	city = models.CharField(max_length = 50)
	venue = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.venue


class Genre(models.Model):
	name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.name

class Band(models.Model):
	name = models.CharField(max_length = 100)
	genres = models.ManyToManyField(Genre)

	def __unicode__(self):
		return self.name

class Show(models.Model):
	genres = models.ManyToManyField(Genre)
	band = models.ManyToManyField(Band)
	date = models.DateTimeField('show date')
	location = models.ForeignKey(Location)

	def __unicode__(self):
		return  self.band.get(id=1).name + " playing at the " + self.location.venue +" in "+ self.location.city

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	shows = models.ManyToManyField(Show)
	bands = models.ManyToManyField(Band)
	location = models.CharField(max_length=50)
	max_distance = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.user.username
