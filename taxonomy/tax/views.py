from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
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


def search(req):
	N=[]
	try:
		text,cat=req.GET['text'],req.GET['cat']
		print(text); print(cat);
	except:
#		raise Http404('404')
		return redirect('index')

	text=text.strip()
	cat=cat.strip()

	if len(cat)==0 and len(text)!=0:
		try:
			print('cat == empty')
			N=Node.objects.filter(name__text__contains=text)[:50]
			print(N.query)
			print(N)
			print(len(N))
		except:
			N=[]
	elif len(text)!=0:
		try:
			print('cat == nonempty')
			N=Node.objects.filter(name__text__contains=text,rank__contains=cat)[:50]
			print(N.query)
			print(N)
			print(len(N))
		except:
			N=[]

	return render(req,'search.html',{'GET':req.GET,'N':N})
