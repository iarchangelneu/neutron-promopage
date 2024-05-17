from django.urls import path
from .views import NewApplication

urlpatterns = [
    path('new-application/', NewApplication.as_view(), name='new-application'),
]