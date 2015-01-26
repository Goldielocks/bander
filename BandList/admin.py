from django.contrib import admin
from BandList.models import Location, Genre, Band, Show, UserProfile
# Register your models here.
admin.site.register(Show)
admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Location)
admin.site.register(UserProfile)
