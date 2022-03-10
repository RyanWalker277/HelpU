from django.contrib import admin
from .models import libraries, places, restraunts, toilets

admin.site.register(places)
admin.site.register(restraunts)
admin.site.register(libraries)
admin.site.register(toilets)
