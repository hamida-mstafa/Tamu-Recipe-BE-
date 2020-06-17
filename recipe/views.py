from django.http import HttpResponse, Http404
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, UpdateProfile
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    current_user = request.user
    return render(request,'profile.html',{"current_user":current_user})

def update_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(request, 'update_profile.html',{"form":form})

def deleteaccount(request):
    current_user = request.user
    account = User.objects.get(pk=current_user.id)
    account.delete()
    return redirect('register')