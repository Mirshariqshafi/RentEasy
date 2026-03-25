from django.contrib import admin
from .models import Property, PropertyPhoto, ContactMessage

admin.site.register(Property)
admin.site.register(PropertyPhoto)
admin.site.register(ContactMessage)