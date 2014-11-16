from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from jobs.models import Job
from linkedin import linkedin

# Create your views here.
def index(request):
    context = {
        'linkedin_auth_url': linkedin.AuthorizationURL.url
    }
    return render(request, 'common/index.html', context)

def auth(request):
    code = linkedin.AccessToken.getCode(request)
    linkedin.AccessToken.sendCode(code)
    return HttpResponse('thanks')

def dashboard(request):
    jobs_list = Job.objects.all()
    context = { 'jobs_list': jobs_list }
    return render(request, 'jobs/index.html', context)