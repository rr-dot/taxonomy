from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('<int:id>/',views.node,name='node'),
	path('random/',views.random,name='random'),
	path('search/',views.search,name='search'),
]

