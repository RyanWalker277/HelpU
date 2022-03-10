from django.contrib import admin
from .models import banks, hospitals, libraries, malls, restraunts, toilets

admin.site.register(restraunts)
admin.site.register(libraries)
admin.site.register(toilets)
admin.site.register(banks)
admin.site.register(hospitals)
admin.site.register(malls)