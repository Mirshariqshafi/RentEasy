from django import forms
from .models import Property, PropertyPhoto, ContactMessage

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'location', 'price', 'property_type', 'bedrooms', 'is_available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = PropertyPhoto
        fields = ['image']

from django import forms
from .models import Property, PropertyPhoto, ContactMessage

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'location', 'price', 'property_type', 'bedrooms', 'is_available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = PropertyPhoto
        fields = ['image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['sender_name', 'sender_email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            # Hide name and email fields for logged in users
            self.fields.pop('sender_name')
            self.fields.pop('sender_email')