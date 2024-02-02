from ..forms.user_forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user_form.save()

            return redirect('list_users')
    else:
        user_form = UserForm()

    return render(request, 'users/user_form.html', {'form_user': user_form})

def list_users(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=True)

    return render(request, 'users/user_list.html', {'users': users})