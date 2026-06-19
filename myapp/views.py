from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CafeContact
from .models import CafeGallery

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    # Database se saari images fetch kar rahe hain
    images = CafeGallery.objects.all()
    context = {
        'gallery_images': images
    }
    return render(request, 'gallery.html', context)

def contact(request):
    if request.method == "POST":
        # Form se data nikaal rahe hain
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Database mein save kar rahe hain
        contact_entry = CafeContact(name=name, email=email, phone=phone, message=message)
        contact_entry.save()

        # Success message setup (Optional but premium look deta hai)
        messages.success(request, "Thank you! Your message has been received with love.")
        return redirect('contact') # Contact page ko reload karega

    return render(request, 'contact.html')