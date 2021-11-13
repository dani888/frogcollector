from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def frogs_index(request):
  return render(request, 'frogs/index.html', { 'frogs': frogs })

class Frog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

frogs = [
  Frog('Lolo', 'tabby', 'foul little demon', 3),
  Frog('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Frog('Raven', 'black tripod', '3 legged frog', 4)
]