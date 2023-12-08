from django.urls import path
from .views import register_service, list_services, edit_services

urlpatterns = [
    path('services/register', register_service, name="register_service"),
    path('services/list', list_services, name='list_services'),
    path('services/edit/<int:id>', edit_services, name='edit_services')
]