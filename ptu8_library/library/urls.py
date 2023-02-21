from django.urls import path
from . import views

# aprasyti visus naudojamus urls
urlpatterns = [
    path("", views.index, name="index") # path, funkcija, funkcijos pavadinimas
]