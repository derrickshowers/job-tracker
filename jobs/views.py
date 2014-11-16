from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from jobs.models import Job

# Create your views here.
def index(request):
    jobs_list = Job.objects.all()
    context = { 'jobs_list': jobs_list }
    return render(request, 'jobs/index.html', context)