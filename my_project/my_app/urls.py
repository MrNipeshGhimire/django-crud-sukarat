from django.urls import path
from .views.main_view import index_method,about_method,add_product,edit_product

urlpatterns = [
    path('', index_method, name="index"),
    path('about/', about_method, name="about"),
    path('add/', add_product, name="add_product"),
    path('edit/',edit_product, name="edit")
]
