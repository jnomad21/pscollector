from django.shortcuts import render
from .models import Game
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
class GameList(ListView):
  model= Game
class GameCreate(CreateView):
  model= Game
  fields= '__all__'
class GameUpdate(UpdateView):
  model= Game
  fields= '__all__'
class GameDelete(DeleteView):
  model=Game
  success_url='/games/'
class GameDetail(DetailView):
  model=Game

# def games_index(request):
#   games=Game.objects.all()
#   return render(request, 'games/index.html', {'games': games})
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', { 'game': game })