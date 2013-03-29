# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard/dashboard.html')
    else:
       return HttpResponseRedirect(reverse("django.contrib.auth.views.login"))

def new_dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'new_dashboard/new_dashboard.html')
    else:
        return HttpResponseRedirect(reverse("django.contrib.auth.views.login"))

