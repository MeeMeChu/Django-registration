from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from app_users.forms import RegisterForm, UserProfileForm, ExtendedProfileForm

# Create your views here.
def register(request: HttpRequest):
    # POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('register_thankyou'))
    else: 
        form = RegisterForm()

    context = {'form' : form }
    return render(request, 'app_users/register.html', context)

def register_thankyou(request: HttpRequest):
    return render(request, 'app_users/register_thankyou.html')

@login_required
def profile(request: HttpRequest):
    user = request.user
    is_new_profile = False
    # POST
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        try:
            # Will Update Profile
            extended_form = ExtendedProfileForm(request.POST, instance=user.profile)
        except:
            # Will Create Profile
            extended_form = ExtendedProfileForm(request.POST)
            is_new_profile = True

        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile:
                # Create New Profile
                profile = extended_form.save(commit=False)
                profile.user = request.user
                profile.save()
            else:
                # Update Profile
                extended_form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        #GET
        form = UserProfileForm(instance=user)
        try:
            extended_form = ExtendedProfileForm(instance=user.profile)
        except:
            extended_form = ExtendedProfileForm()
    context = {
        'form' : form,
        'extended_form' : extended_form
    }
    return render(request, 'app_users/profile.html', context)