from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import PetForm

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

def new_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            pet = form.save(commit=False)

            pet.user_id = request.user
            pet.save()
            return redirect('detail_pet', pk=pet.pk)
    else:
        form = PetForm()
    return render(request, 'pet/new_pet.html', {'form': form})

def edit_pet(request,pk):
    pet = get_object_or_404(Pet, pk=pk, user_id= request.user)

    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            return redirect('detail_pet', pk=pet.pk)
    else:
        form = PetForm(instance=pet)
    return render(request, 'pet/new_pet.html', {'form': form})

def delete_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    if pet.user_id == request.user:
        pet.delete()
        return redirect('my_pets')
    return redirect('detail_pet', pk=pet.pk)

    #manda mesagem de voce nao possui esse pet