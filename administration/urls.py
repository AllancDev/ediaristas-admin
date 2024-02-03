from django.urls import path
from django.urls.base import reverse_lazy
from .views import service_views, user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('services/register', service_views.register_service, name="register_service"),
    path('services/list', service_views.list_services, name='list_services'),
    path('services/edit/<int:id>', service_views.edit_services, name='edit_services'),

    path('users/register', user_views.register_user, name='register_user'),
    path('users/list', user_views.list_users, name='list_users'),
    path('users/edit/<int:id>', user_views.update_user, name="edit_user"),

    path('auth/login', auth_views.LoginView.as_view(), name="auth_user"),
    path('auth/logout', auth_views.LogoutView.as_view(), name="logout_user" ),

    path('forgot_password', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('list_services')), name="forgot_password" ),

    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password/success', auth_views.PasswordResetDoneView.as_view(), name="reset_password_sucess"),
    path('reset_password/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(), name="reset_password_confirm"),
    path('reset_password/done', auth_views.PasswordResetDoneView.as_view(), name="reset_password_done")
]