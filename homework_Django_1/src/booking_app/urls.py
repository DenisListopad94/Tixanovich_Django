from django.urls import path, include
from .views import main_view, info_view

urlpatterns = [
    path('main', main_view),
    path('info', info_view),
]
