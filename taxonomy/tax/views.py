from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.template import loader

# Create your views here.

def index(req):
	return render(req,'index.html')

def node(req,id):
	try:
		n=Node.objects.get(pk=id)
	except:
		raise Http404("Does not exist")
	h=[n]
	while True:
		x=h[-1]
		if x.pk==1: break
		x=x.p
		h.append(x)

	h.reverse() # heritage (path from root to current node for breadcrumb menu)
	return render(req,'node.html',{'n':n,'chd':Node.objects.filter(p_id=n.pk),'h':h})

#how to get child nodes
#
#>>> for c in Node.objects.filter(p_id=9691):
#...     print(c.name.text)
#...
#Panthera pardus orientalis
#Panthera pardus saxicolor
#Panthera pardus japonensis
#Panthera pardus fusca
#Panthera pardus fontanierii
#Panthera pardus kotiya
#Panthera pardus tulliana
#
# here p_id is the id whose children we are finding

def random(req):
	n=Node.objects.order_by("?").first()
	return redirect('node',id=n.pk)

