from django.urls import path
from . import views
# from books.views import BookList

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('frogs/', views.frogs_index, name='index'),
#   path('frogs/<int:frog_id>/', views.frog_detail, name='detail'),
  # new route used to show a form and create a cat
  path('frogs/create/', views.FrogCreate.as_view(), name='frogs_create'),
]