from django.shortcuts import render
from django.views import generic


class LP(generic.TemplateView):
	template_name = 'amazon/lp.html'
