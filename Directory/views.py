from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Directory.models import Directory
from django.contrib.auth.models import User
from Page.models import Page
from .serializers import DirectorySerializer
from rest_framework import viewsets
from .forms import DirectoryModelForm, ShareDirectoryForm, UserSearchForm


class DirectoryViewSet(viewsets.ModelViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


@login_required
def view_directories(request, pid):
    # print(pid)
    parent = Directory.objects.get(pk=pid)
    if parent.user == request.user:
        ds = Directory.objects.filter(user=request.user, parent=parent)
        # print(ds)
        ps = Page.objects.filter(user=request.user, directory=parent)
        path = []
        while parent:
            path.insert(0, parent)
            parent = parent.parent
        search_form = UserSearchForm()
        return render(request, "viewdirectories.html", {'directories': ds,
                                                    'path': path,
                                                    'pages': ps,
                                                    'parent': parent,
                                                    'search_form': search_form})
    else:
        return HttpResponse('<h1>Cannot open a directory you don\'t have excess to!!!</h1>')


def create_directory(request, pid):
    parent = Directory.objects.get(pk=pid)
    if parent.user.username != request.user.username:
        print("privacy bro!")
        print(parent.user.username)
        print(request.user.username)
        return redirect('/admin')
    print("same user bro! welcome!!!")
    if request.method == 'POST':
        directory_form = DirectoryModelForm(request.POST)
        if directory_form.is_valid():
            directory_name = directory_form.cleaned_data['name']
            directory_subject = directory_form.cleaned_data['subject']
            d = Directory(user=request.user, name=directory_name, subject=directory_subject, parent=parent)
            d.save()
            return redirect('/'+str(d.pk)+'/')
    else:
        directory_form = DirectoryModelForm()

    search_form = UserSearchForm()
    return render(request, 'create_directory.html', {'directory_form': directory_form,
                                                     'search_form': search_form})


def send_directory(request, pid):
    parent = Directory.objects.get(pk=pid)
    if parent.user.username != request.user.username:
        print("can\'t share what ain\'t yours bruh!!")
        return redirect('/admin')
    print('hey man! sharing stuff i see!')
    if request.method == "POST":
        sharing_form = ShareDirectoryForm(request.POST)
        if sharing_form.is_valid():
            user_name = sharing_form.cleaned_data['user_name']
            share_with = User.objects.get(username=user_name).username
            share_contents(parent, share_with, None)
            return redirect('/'+str(pid)+'/')
        else:
            return HttpResponse('<h1>Invalid Form</h1>')
    else:
        sharing_form = ShareDirectoryForm()

    search_form = UserSearchForm()
    return render(request, 'share_directory.html', {'sharing_form': sharing_form,
                                                    'search_form': search_form})


def share_contents(current, username, parent):
    user = User.objects.get(username=username)
    pages = Page.objects.filter(directory=current)
    d = Directory(user=user, name=current.name, subject=current.subject, parent=parent)
    d.save()
    directories = Directory.objects.filter(parent=current)
    for i in pages:
        p = Page(user=user, title=i.title, comments=i.comments, link=i.link, directory=d)
        p.save()

    for i in directories:
        share_contents(i, username, d)


def delete_directory(request, pid):
    d = Directory.objects.get(pk=pid)
    parent = d.parent
    d.delete()
    return redirect('/'+str(parent.pk)+'/')


def update_directory(request, pid):
    directory = Directory.objects.get(pk=pid)
    if request.method == 'POST':
        update_form = DirectoryModelForm(request.POST)
        if update_form.is_valid():
            name = update_form.cleaned_data['name']
            subject = update_form.cleaned_data['subject']
            directory.update(name=name, subject=subject)
            return redirect('/{{directory.pk}}/')
        else:
            return redirect('/{{directory.pk}}/update-directory/')
    else:
        update_form = DirectoryModelForm(initial={'name': directory.name,
                                                  'subject': directory.subject})
    return render(request, 'edit_directory.html', {'update_form': update_form})
