from django.shortcuts import render
from .models import Pet
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    if request.method == 'POST':
        search_pet = request.POST.get('search')

        if search_pet:
            pet_list = Pet.objects.filter(city_icontains=search_pet)
            paginator = Paginator(pet_list, 8)
            page = request.GET.get('page')
            data = {'pets': paginator.get_page(page)}

            return render(request, 'pet/home.html', data)

    pet_list = Pet.objects.all().order_by('-begin_date')
    paginator = Paginator(pet_list, 8)
    page = request.GET.get('page')
    data = {'pets': paginator.get_page(page)}
    return render(request, 'pet/home.html', data)