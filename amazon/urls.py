from django.urls import path
from . import views


app_name = 'amazon'

urlpatterns = [
	path('lp', views.LP.as_view(), name='lp'),
	path('items/', views.Itemlist.as_view(), name='item_list'),
	path('item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
]

