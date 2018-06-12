from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from inventory import views as inventory_views
from order import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/shops/<int:pk>',
         inventory_views.ShopDetailView.as_view(), name='shop_detail'),
    path('api/v1/orders/<int:pk>',
         order_views.OrderDetailView.as_view(), name='order_detail'),
    path('api/v1/items',
         order_views.CreateOrderItemView.as_view(), name='create_order_item'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
