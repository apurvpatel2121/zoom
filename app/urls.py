from django.urls import path
from app.views import *

urlpatterns = [
	path('list/',list,name="list"),
	path('',all,name="all"),
	path('create/',create,name="create")
]
