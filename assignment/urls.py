from django.urls import path
from internship import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_category/', views.add_category, name='add_category'),
    path('update_category/<int:category_id>/', views.update_category, name='update_category'),
    path('add_product/', views.add_product, name='add_product'),
]
