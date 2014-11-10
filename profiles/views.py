#from django.shortcuts import render

#from django.contrib.auth.models import User
from django.shortcuts import render_to_response , RequestContext#, Http404, HttpResponseRedirect

def home(request):
	return render_to_response('home.html', locals(), context_instance=RequestContext(request))