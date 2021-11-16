from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Frog
from .forms import FeedingForm

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def frogs_index(request):
  frogs = Frog.objects.all()
  return render(request, 'frogs/index.html', { 'frogs': frogs })

def frogs_detail(request, frog_id):
  frog = Frog.objects.get(id=frog_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'frogs/detail.html', {
    # include the cat and feeding_form in the context
    'frog': frog, 'feeding_form': feeding_form
  })

def add_feeding(request, frog_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.frog_id = frog_id
    new_feeding.save()
  return redirect('detail', frog_id=frog_id)

class FrogCreate(CreateView):
  model = Frog
  fields = '__all__'
  success_url = '/frogs/'

class FrogUpdate(UpdateView):
  model = Frog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class FrogDelete(DeleteView):
  model = Frog
  success_url = '/frogs/'

# class Frog:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# frogs = [
#   Frog('Lolo', 'tabby', 'foul little demon', 3),
#   Frog('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Frog('Raven', 'black tripod', '3 legged frog', 4)
# ]