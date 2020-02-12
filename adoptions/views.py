from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pet

def home(request):
  pets = Pet.objects.all()
  return render(request, 'home.html', {'pets': pets})

def pet_detail(request, id):
  # return HttpResponse('<p>pet detail view with the id {}'.format(id))
  try: 
    pet = Pet.objects.get(id=id)
  except Pet.DoesNotExist:
    raise Http404('Pet not found')
  return render(request, 'pet_detail.html', {'pet': pet})