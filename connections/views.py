from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from connections.models import Connection
from linkedin import linkedin

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        connections_list = linkedin.refreshConnections(request.user)
        print(connections_list)
        context = { 'connections_list': connections_list }
        return render(request, 'connections/index.html', context)
    else:
        return redirect('jobtracker.views.index')