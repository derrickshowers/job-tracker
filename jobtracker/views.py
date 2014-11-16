from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from jobs.models import Job
from linkedin import linkedin

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')
    else:
        context = { 'linkedin_auth_url': linkedin.AuthorizationURL.url }
        return render(request, 'common/index.html', context)

def auth(request):
    code = linkedin.AccessToken.getCode(request)
    user = linkedin.AccessToken.sendCode(code)

    # TODO: Make this more secure than just setting 'password' as the passowrd
    authUser = authenticate(username=user.username, password='password')
    login(request, authUser)
    return redirect('/dashboard/')

def dashboard(request):
    if request.user.is_authenticated():
        jobs_list = Job.objects.all()
        context = { 'jobs_list': jobs_list }
        return render(request, 'jobs/index.html', context)
    else:
        return redirect('/')

def userLogout(request):
    logout(request)
    return redirect('/')