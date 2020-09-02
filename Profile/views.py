from django.shortcuts import render, redirect, HttpResponse
from .forms import ProfileForm, UpdateProfileForm, UserSearchForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from Directory.models import Directory
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            name = profile_form.cleaned_data["name"]
            mail = profile_form.cleaned_data["mail"]
            birth_date = profile_form.cleaned_data["birth_date"]
            gender = profile_form.cleaned_data["gender"]
            user = User.objects.get(username=user_form.cleaned_data["username"])
            d = Directory(user=user, name=user.username + "-root", subject="Root Directory")
            d.save()
            p = Profile(user=user, name=name, mail=mail, birth_date=birth_date,
                        gender=gender, root_directory=d)
            p.save()
            return redirect("/login")
        else:
            return HttpResponse('<h1>Invalid Form</h1>')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()

    return render(request, "register.html", {'user_form': user_form, 'profile_form': profile_form})


def my_profile(request, username):
    user_pk = User.objects.get(username=username)
    return redirect('/view-profile/'+str(user_pk))


def homepage(request):
    directories = Directory.objects.filter(user=request.user, parent=None)
    search_form = UserSearchForm()
    return render(request, "homepage.html", {'user': request.user, 'directories': directories, 'search_form': search_form})


@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, instance=user.profile)
        if profile_form.is_valid():
            name = profile_form.cleaned_data["name"]
            mail = profile_form.cleaned_data["mail"]
            birth_date = profile_form.cleaned_data["birth_date"]
            gender = profile_form.cleaned_data["gender"]
            location = profile_form.cleaned_data["location"]
            Profile.objects.filter(user=user).update(name=name, mail=mail,
                                                     birth_date=birth_date, gender=gender,
                                                     location=location)
            # p.save()
            return redirect('/update-profile/')
        else:
            return HttpResponse('<h1>Invalid Form</h1>')
    else:
        profile_form = UpdateProfileForm(initial={'name': user.profile.name,
                                                  'mail': user.profile.mail,
                                                  'birth_date': user.profile.birth_date,
                                                  'gender': user.profile.gender,
                                                  'location': user.profile.location,})

    search_form = UserSearchForm()
    return render(request, "updateprofile.html", {'profile_form': profile_form,
                                                  'search_form': search_form})

@login_required
def go_to_root(request):
    p = Profile.objects.get(user=request.user)
    root = p.root_directory
    return redirect('/'+str(root.pk)+'/')


@login_required
def view_profile(request, pk):
    user = User.objects.get(pk=pk)
    profile = user.profile
    search_form = UserSearchForm()
    if profile.gender == "M":
        gender = "Male"
    elif profile.gender == "F":
        gender = "Female"
    else:
        gender = "Other"
    return render(request, "viewprofile.html", {'user': user,
                                                'profile': profile,
                                                'search_form': search_form,
                                                'gender': gender})


def find_user(request):
    if request.method == 'POST':
        search_form = UserSearchForm(request.POST)
        if search_form.is_valid():
            username = search_form.cleaned_data["username"]
            try:
                user = User.objects.get(username=username)
            except:
                return HttpResponse('<h1>User not found</h1>')
            return redirect(view_profile, pk=user.pk)
        else:
            return HttpResponse('<h1>Invalid Form</h1>')
