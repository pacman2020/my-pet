from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    if request.method == 'POST':
        search_pet = request.POST.get('search')

        if search_pet:
            pet_list = Pet.objects.filter(city=search_pet)
            paginator = Paginator(pet_list, 8)
            page = request.GET.get('page')
            data = {'pets': paginator.get_page(page)}

            return render(request, 'pet/home.html', data)

    pet_list = Pet.objects.all().order_by('-begin_date')
    paginator = Paginator(pet_list, 8)
    page = request.GET.get('page')
    data = {'pets': paginator.get_page(page)}
    return render(request, 'pet/home.html', data)

def my_pets(request):
    if request.method == 'POST':
        search_pet = request.POST.get('search')

        if search_pet:
            pet_list = Pet.objects.filter(
                Q(city=search_pet),
                Q(user_id=request.user.id)
                )
            paginator = Paginator(pet_list, 8)
            page = request.GET.get('page')
            data = {'pets': paginator.get_page(page)}

            return render(request, 'pet/home.html', data)

    pet_list = Pet.objects.all().order_by('-begin_date').filter(user_id=request.user.id)
    paginator = Paginator(pet_list, 8)
    page = request.GET.get('page')
    data = {'pets': paginator.get_page(page)}
    return render(request, 'pet/home.html', data)

def detail_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    data = {'pet': pet}
    return render(request, 'pet/detail_pet.html', data)