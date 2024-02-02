from django.urls import path
from .views import service_views, user_views

urlpatterns = [
    path('services/register', service_views.register_service, name="register_service"),
    path('services/list', service_views.list_services, name='list_services'),
    path('services/edit/<int:id>', service_views.edit_services, name='edit_services'),
    path('users/register', user_views.register_user, name='register_user'),
    path('users/list', user_views.list_users, name='list_users'),
]