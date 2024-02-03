from ..forms.user_forms import RegisterUserForm, UpdateUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def register_user(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)

        if user_form.is_valid():
            user_form.save()

            return redirect('list_users')
    else:
        user_form = RegisterUserForm()

    return render(request, 'users/user_form.html', {'form_user': user_form})

def list_users(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=True)

    return render(request, 'users/user_list.html', {'users': users})

def update_user(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)

    form_user = UpdateUserForm(request.POST or None, instance=user)

    if form_user.is_valid():
        form_user.save()
        return redirect('list_users')
    
    return render(request, 'users/user_form.html', {'form_user': form_user})