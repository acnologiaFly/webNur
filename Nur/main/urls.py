from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('product/<int:product_id>/', views.product_details, name='product'),
    path('order/<int:product_id>/', views.order, name='order'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
