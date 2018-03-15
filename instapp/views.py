from django.shortcuts import render,redirect
from . forms import RegistrationForm,EditProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/instapp/login/')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'reg_form.htm',args)
@login_required
def view_profile(request):

    arg = {'user': request.user}

    return render(request, 'profile.html')
@login_required
def edit_profile(request):
    if request.method=='POST':
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else: 
        form = EditProfile(instance=request.user)
        args = {'form':form}
        return render(request, 'edit_profile.htm',args)
@login_required      
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/instapp/profile')
        else:
            redirect('change_password')
    else: 
        form = PasswordChangeForm(user=request.user)

        args = {'form':form}
        return render(request, 'change_password.htm',args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)


def search_results(request):
    
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
