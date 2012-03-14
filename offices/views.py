from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render_to_response
from django.template import RequestContext

from offices.models import Office
from offices.forms import OfficeForm

@login_required
def add(request):
    form = OfficeForm()
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid:
            new_office = form.save()
            return HttpResponseRedirect('/offices/all/')
    return render_to_response('offices/add.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def list(request):
    offices = Office.objects.filter(time_deleted=None)
    paginator = Paginator(offices, 5)
    return render_to_response('offices/list.html', {
        'paginator': paginator,
    }, context_instance=RequestContext(request))
