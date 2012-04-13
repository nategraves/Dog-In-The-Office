from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile')
    return render_to_response('index/index.html',{
            }, context_instance=RequestContext(request))
