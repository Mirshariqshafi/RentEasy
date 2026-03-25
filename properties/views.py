from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Property, PropertyPhoto, ContactMessage
from .forms import PropertyForm, PhotoForm, ContactForm

# Homepage — shows all available properties
def home(request):
    properties = Property.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'properties/home.html', {'properties': properties})

# Property detail — shows one property with photos and contact form
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    photos = property.photos.all()
    form = ContactForm(user=request.user)  # pass user so form knows who is logged in

    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.property = property

            # If user is logged in, use their credentials automatically
            if request.user.is_authenticated:
                contact.sender_name = request.user.get_full_name() or request.user.username
                contact.sender_email = request.user.email

            contact.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('property_detail', pk=pk)

    return render(request, 'properties/property_detail.html', {
        'property': property,
        'photos': photos,
        'form': form
    })

# Owner posts a new property
@login_required
def post_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)

        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user  # set owner to logged in user
            property.save()

            # Save multiple uploaded photos
            for photo in request.FILES.getlist('image'):
                PropertyPhoto.objects.create(property=property, image=photo)

            messages.success(request, 'Property posted successfully!')
            return redirect('home')
    else:
        form = PropertyForm()

    return render(request, 'properties/post_property.html', {'form': form})

# Owner sees their own listings
@login_required
def my_listings(request):
    properties = Property.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'properties/my_listings.html', {'properties': properties})

# Owner deletes a property
@login_required
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk, owner=request.user)
    property.delete()
    messages.success(request, 'Property deleted.')
    return redirect('my_listings')

# Owner sees all messages received on their properties
@login_required
def my_messages(request):
    messages_received = ContactMessage.objects.filter(
        property__owner=request.user
    ).order_by('-sent_at')

    return render(request, 'properties/my_messages.html', {
        'messages_received': messages_received
    })

@login_required
def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk, owner=request.user)  # only owner can edit
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)  # instance means "edit this existing one"
        if form.is_valid():
            form.save()
            messages.success(request, 'Property updated successfully!')
            return redirect('my_listings')
    else:
        form = PropertyForm(instance=property)  # pre-fill form with current values
    
    return render(request, 'properties/edit_property.html', {
        'form': form,
        'property': property
    })