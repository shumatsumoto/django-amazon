from django.urls import path
from . import views


app_name = 'amazon'

urlpatterns = [
	path('lp', views.LP.as_view(), name='lp'),
]
