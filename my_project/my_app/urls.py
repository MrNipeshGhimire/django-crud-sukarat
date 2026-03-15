from django.urls import path
from .views.main_view import index_method,about_method

urlpatterns = [
    path('', index_method, name="index"),
    path('about/', about_method, name="about")
]
