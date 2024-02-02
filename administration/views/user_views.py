from ..forms.user_forms import UserForm
from django.shortcuts import render


def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserForm()

    return render(request, 'users/user_form.html', {'form_user': user_form})