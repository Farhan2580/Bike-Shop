from django.urls import path
from .import views
urlpatterns = [
    path('add_products', views.add_products, name='add_products'),
    path('update_products/<int:p_id>', views.update_products, name='update_products'),
    path('delete_products/<int:p_id>', views.delete_products, name='delete_products'),

]