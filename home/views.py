from django.shortcuts import render
import os
import demo.settings as settings
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.
def home(request):
    """
    Render the home page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Rendered home page.
    """
    return render(request, 'home.html')

def about(request):
    """
    Render the about page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Rendered about page.
    """
    context = {}
    reviews = []
    images = []

    # Iterate through the static directory to find files starting with 'review'
    for file in os.listdir(settings.STATICFILES_DIRS[0]):
        if file.startswith("review"):
            reviews.append(file)  # Add the file name to the reviews list

    about_us_path = os.path.join(settings.STATICFILES_DIRS[0], "About_Us")
    for file in os.listdir(about_us_path):
        if os.path.isfile(os.path.join(about_us_path, file)):
            images.append(file)  # Add only the file name to the images list

    # Add the reviews and images lists to the context
    context['reviews'] = reviews
    context['images'] = images
    return render(request, 'about.html', context=context)

def contact(request):
    """
    Render the contact page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Rendered contact page.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Send an email notification
        subject = "New Contact Message"
        body = f"Name: {name}\nEmail: {email}\nDoubt: {message}"
        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.RECEIVER_EMAIL_FOR_CONTACT_FORM],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")
    context = {"phone_number": settings.TEACHER_CONTACT_NUMBER}
    return render(request, 'contact.html', context=context)

def gallary(request):
    """
    Render the gallery page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Rendered gallery page.
    """

    context = {'Artist': []}

    # Iterate through each folder in the static directory
    for folder in os.listdir(settings.STATICFILES_DIRS[0]):
        folder_path = os.path.join(settings.STATICFILES_DIRS[0], folder)
        if os.path.isdir(folder_path):  # Check if it's a directory
            images = []
            for file in os.listdir(folder_path):
                images.append(f'{folder}/{file}')
            context[folder] = images  # Add images list to context with folder name as key

    for file in os.listdir(f"{settings.STATICFILES_DIRS[0]}/Artist's_Work/"):
        context.get("Artist").append(f"Artist's_Work/{file}")

    return render(request, 'gallary.html', context=context)

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        parent_name = request.POST.get('p_name')
        whatsapp_number = request.POST.get('w_no')
        age_group = request.POST.get('age_b_10')
        mode_of_class = request.POST.get('oline')
        preferred_days = request.POST.get('day')
        preferred_time = request.POST.get('pr_time')
        mediums = request.POST.getlist('medium')

        subject = "New Registration Details"
        message = f"""
        New registration details have been submitted:
        Name: {name}
        Parent's Name: {parent_name}
        WhatsApp Number: {whatsapp_number}
        Age Group: {age_group}
        Mode of Class: {mode_of_class}
        Preferred Days: {preferred_days}
        Preferred Time: {preferred_time}
        Mediums: {', '.join(mediums)}
        """
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.RECEIVER_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Registration details sent successfully!')
        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")
        
    return render(request, 'register.html')

def courses(request):
    return render(request, "courses.html")

def act(request):
    """
    Render the activity page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Rendered activity page.
    """
    context = {"workshops": [], "exhibition": []}
    for file in os.listdir(f"{settings.STATICFILES_DIRS[0]}/Workshop/"):
        context.get("workshops").append(f"{file}")
    for file in os.listdir(f"{settings.STATICFILES_DIRS[0]}/Exhibition/"):
        context.get("exhibition").append(f"{file}")
    return render(request, "activity.html", context=context)

def robots(request):
    """
    Render the robots.txt file.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Rendered robots.txt file.
    """
    content = render_to_string("robots.txt")
    return HttpResponse(content, content_type="text/plain")


