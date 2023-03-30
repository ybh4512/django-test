from django.shortcuts import render, redirect, HttpResponse
from django.forms.models import model_to_dict

from .models import AdminUser
from .forms import AdminUserForm

import datetime

# Create your views here.
def test(request):
    return render(request, "test.html")

def index(request):
    admin_users = AdminUser.objects.all()
    context = { "admin_users" : admin_users }

    return render(request, "index.html", context)

    # return HttpResponse("<p>Hello Django</p>")


def show(request, admin_user_id):
    admin_user = AdminUser.objects.get(pk=admin_user_id)
    context = { "admin_user" : admin_user }

    return render(request, "show.html", context)


def new(request):
    f = AdminUserForm()
    return render(request, "new.html", {'form': f})


def edit(request, admin_user_id):
    admin_user = AdminUser.objects.get(pk=admin_user_id)
    f = AdminUserForm(instance=admin_user)
    return render(request, "edit.html", {'form':f, "admin_user_id":admin_user_id})


def create(request):
    if not request.POST:
        return redirect("/admin_user/new/")

    form = AdminUserForm(request.POST)
    if not form.is_valid():
        return redirect("/admin_user/new/")

    new_user = AdminUser()
    new_user.name = form.cleaned_data['name']
    new_user.email = form.cleaned_data['email']
    new_user.is_valid = form.cleaned_data['is_valid']
    new_user.description = form.cleaned_data['description']
    new_user.just_datetime = form.cleaned_data['just_datetime']
    new_user.save()

    return redirect("/admin_user/{}/".format(new_user.id))


def update(request, admin_user_id):
    if not request.POST:
        return redirect("/admin_user/{}/edit/".format(admin_user_id))

    form = AdminUserForm(request.POST)
    if not form.is_valid():
        return redirect("/admin_user/{}/edit/".format(admin_user_id))

    user = AdminUser.objects.get(pk=admin_user_id)
    user.name = form.cleaned_data['name']
    user.email = form.cleaned_data['email']
    user.is_valid = form.cleaned_data['is_valid']
    user.description = form.cleaned_data['description']
    user.just_datetime = form.cleaned_data['just_datetime']
    user.save()

    return redirect("/admin_user/{}/".format(admin_user_id))

def delete(request, admin_user_id):
    if not request.POST:
        return redirect("/admin_user/")

    user = AdminUser.objects.get(pk=admin_user_id)
    user.delete()

    return redirect("/admin_user/")

def today_is(request):
    now = datetime.datetime.now()
    html = "<html><body>Current date and time : {0}</body></html>".format(now)
    return HttpResponse(html)


def profile(request, username):
    return HttpResponse("<p>Profile page of #{}</p>".format(username))