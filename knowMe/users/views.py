from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signUp(req):
    if req.method=='POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    context = {
        'form':form,
    }
    return render(req,'users/signup.html', context )

def logOut(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(req):
    if req.method=='POST':
        uForm = UserUpdateForm(req.POST or None, instance = req.user)
        pForm = ProfileUpdateForm(req.POST or None, req.FILES or None, instance=req.user.profilemodel)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            return redirect('profile')
    else:
        uForm = UserUpdateForm(instance = req.user)
        pForm = ProfileUpdateForm(instance=req.user.profilemodel)
    context = {
        'uForm':uForm,
        'pForm':pForm,
    }
    return render(req, 'users/profile.html', context)