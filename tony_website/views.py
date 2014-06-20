# Create views here

import json
import re
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext

def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))

