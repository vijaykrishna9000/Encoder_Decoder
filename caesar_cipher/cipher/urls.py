from django.urls import path
from . import views

app_name = "cipher"
urlpatterns = [
    path("", views.cipher_view, name="index"),
]