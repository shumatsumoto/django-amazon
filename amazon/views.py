from django.shortcuts import render
from django.views import generic
from .models import *


class LP(generic.TemplateView):
	template_name = 'amazon/lp.html'


class Itemlist(generic.ListView):
	model = Product
	template_name = 'amazon/item_list.html'

	def get_queryset(self):
		products = Product.objects.all()
		if 'q' in self.request.GET and self.request.GET['q'] != None:
			q = self.request.GET['q']
			products = products.filter(name__icontains = q)
		return products
	