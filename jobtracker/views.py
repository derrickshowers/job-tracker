from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from jobs.models import Job
from linkedin import linkedin

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return redirect('jobtracker.views.dashboard')
    else:
        context = { 'linkedin_auth_url': linkedin.getAuthorizationURL() }
        return render(request, 'common/index.html', context)

def auth(request):
    # get the user from the 'code' param in the url
    user = linkedin.storeLinkedinUser(linkedin.getCode(request))

    # TODO: Make this more secure than just setting 'password' as the passowrd
    # authenticate user
    authUser = authenticate(username=user.username, password='password')

    # log him/her/it in if all is good
    if authUser is not None:
        login(request, authUser)
    else:
        redirect('/?error=notAuthorized')

    # redirect to dashboard if all is good
    return redirect('jobtracker.views.dashboard')

def dashboard(request):
    if request.user.is_authenticated():
        linkedin.refreshConnections(request.user)
        jobs_list = Job.objects.all()
        context = { 'jobs_list': jobs_list }
        return render(request, 'common/dashboard.html', context)
    else:
        return redirect('jobtracker.views.index')

def userLogout(request):
    logout(request)
    return redirect('jobtracker.views.index')