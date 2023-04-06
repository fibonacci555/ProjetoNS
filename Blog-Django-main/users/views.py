from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Your Account has been created, You are now able to Login')
            profile, created = Profile.objects.get_or_create(user=user)
            profile.save()
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
@login_required
def profile(request):
    if request.method == 'POST':
     
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
           
            p_form.save()
            messages.success(request, f'Your Account has been Updated')
            return redirect('profile')
    else:
   
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)