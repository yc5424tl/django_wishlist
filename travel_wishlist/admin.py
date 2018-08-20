from django.contrib import admin
from .models import Place

admin.site.register(Place)  # Adding our 'Place' model to Django's admin console for our own use
