from django.shortcuts import render
from django.views import generic
from .models import *


class LP(generic.TemplateView):
	template_name = 'amazon/lp.html'

	def get_context_data(self, **kwargs):
		context = super(LP, self).get_context_data(**kwargs)
		all_items = Product.objects.all()
		context["items"] = all_items 
		return context
	

class Itemlist(generic.ListView):
	model = Product
	template_name = 'amazon/item_list.html'

	def get_queryset(self):
		products = Product.objects.all()
		if 'q' in self.request.GET and self.request.GET['q'] != None:
			q = self.request.GET['q']
			products = products.filter(name__icontains = q)
		return products


class ItemDetail(generic.DetailView):
	model = Product
	template_name = 'amazon/item_detail.html'

