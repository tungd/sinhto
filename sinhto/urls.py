from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from order import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/orders', order_views.OrderListView.as_view(), name='order_list'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
