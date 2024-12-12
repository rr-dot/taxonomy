from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from . import views
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect

User = get_user_model()

def CustomMiddleware(get_response):
	print('CustomMiddleware')
	@csrf_protect
	def middleware(req):
#		if req.path=='/login': return get_response(req)
		print('executing middleware():')
		print('is auth: ',req.user.is_authenticated)
		if True:
			print('is logged in')
			if req.user.is_authenticated:
				if req.user.is_superuser:
					myreq=req.POST.copy()
					myreq['style']='font-weight:bold;'
					req.POST=myreq
					print('Modified req')
		print('CustomMiddleware middleware(): req = ',req)
		print(req.POST)
		return get_response(req)

	return middleware
