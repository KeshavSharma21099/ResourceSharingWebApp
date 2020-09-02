from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Page
from rest_framework import viewsets
from .serializers import PageSerializer
from .forms import NewPageForm, UserSearchForm
from Directory.models import Directory
from Profile.models import Profile


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


def new_page(request, pid):
    if request.method == "POST":
        parent = Directory.objects.get(pk=pid)
        page_form = NewPageForm(request.POST)
        if page_form.is_valid():
            page_title = page_form.cleaned_data['title']
            page_comment = page_form.cleaned_data['comments']
            page_link = page_form.cleaned_data['link']
            user = request.user
            p = Page(user=user, title=page_title, link=page_link, comments=page_comment, directory=parent)
            p.save()
            return redirect('/'+str(pid)+'/')
        else:
            return HttpResponse('<h1>Invalid Form</h1>')
    else:
        page_form = NewPageForm()
    return render(request, "new_page.html", {'page_form': page_form})


def send_page(request, pid):
    p = Page.objects.get(pk=pid)
    dir_pk = p.directory.pk
    if request.method == 'POST':
        sharing_form = UserSearchForm(request.POST)
        if sharing_form.is_valid():
            username = sharing_form.cleaned_data['username']
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            root = profile.root_directory
            page = Page(user=user, title=p.title, comments=p.comments, link=p.comments, directory=root)
            page.save()
            return redirect('/'+str(dir_pk)+'/')
        else:
            return HttpResponse('<h1>Invalid Form</h1>')
    else:
        sharing_form = UserSearchForm()

    return render(request, "share_page.html", {'sharing_form': sharing_form})


def instant_share(request):
    if request.method == 'POST':
        user_form = UserSearchForm(request.POST)
        page_form = NewPageForm(request.POST)
        if user_form.is_valid() and page_form.is_valid():
            username = user_form.cleaned_data['username']
            user = User.objects.get(username=username)
            if not user:
                return HttpResponse('<h1>Not a valid User!!!</h1>')
            else:
                title = page_form.cleaned_data['title']
                comments = page_form.cleaned_data['comments']
                link = page_form.cleaned_data['link']
                profile = Profile.objects.get(user=user)
                root = profile.root_directory
                p = Page(user=user, title=title, comments=comments, link=link, directory=root)
                p.save()
                return redirect('/'+str(root.pk)+'/')
        else:
            return HttpResponse('<h1>Invalid Form</h1>')
    else:
        user_form = UserSearchForm()
        page_form = NewPageForm()
    return render(request, 'instant_share.html', {'user_form': user_form,
                                                  'page_form': page_form})


def delete_page(request, pid):
    p = Page.objects.get(pk=pid)
    directory = p.directory
    p.delete()
    return redirect('/'+str(directory.pk)+'/')
