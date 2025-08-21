# circles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm # Import the new form
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BlogPost

# Make sure this function exists and is named 'home'
@login_required 
def home(request):
    user_circles = request.user.joined_circles.all()
    posts = BlogPost.objects.filter(circle__in=user_circles).order_by('-created_at')

    context = {
        'posts': posts
    }
    return render(request, 'circles/home.html', context)
# ... your existing home view ...

def register(request):
    if request.method == 'POST':
        # Process the submitted form data
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Save the new user to the database
            login(request, user) # Log the user in automatically
            return redirect('home') # Redirect to the home page
    else:
        # Display a blank registration form
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})