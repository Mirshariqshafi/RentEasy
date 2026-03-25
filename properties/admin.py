from django.contrib import admin
from .models import Property, PropertyPhoto, ContactMessage

class PhotoInline(admin.TabularInline):
    model = PropertyPhoto
    extra = 0  # Don't show empty extra photo slots

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'location', 'price', 'property_type', 'bedrooms', 'is_available', 'created_at']
    list_filter = ['is_available', 'property_type']   # Filter sidebar on the right
    search_fields = ['title', 'location', 'owner__username']  # Search bar at top
    inlines = [PhotoInline]  # Show photos directly inside a property page

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'sender_email', 'property', 'property_owner', 'sent_at']
    search_fields = ['sender_name', 'sender_email', 'property__title']
    readonly_fields = ['sender_name', 'sender_email', 'message', 'property', 'sent_at']  # Prevent accidental edits

    # Custom column showing which owner the message was sent to
    def property_owner(self, obj):
        return obj.property.owner.username
    property_owner.short_description = 'Property Owner'  # Column header name

admin.site.register(Property, PropertyAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)