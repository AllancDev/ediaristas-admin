from django.shortcuts import render, redirect
from .forms import ServiceForm
from .models import Service

# Create your views here.
def register_service(request):
    if request.method == "POST":
        form_service = ServiceForm(request.POST)
        if form_service.is_valid():
            form_service.save()
            return redirect('list_services')
    else:
        form_service = ServiceForm
    return render(request, 'services/form_service.html', {'form_service': form_service })

def list_services(request):
    services = Service.objects.all()
    
    return render(request, 'services/list_services.html', {'services': services})

def edit_services(request, id):
    service = Service.objects.get(id=id)
    form_service = ServiceForm(request.POST or None, instance=service)

    if form_service.is_valid():
        form_service.save()
        return redirect('list_services')

    return render(request, 'services/form_service.html', {'form_service': form_service})