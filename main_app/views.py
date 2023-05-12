from django.shortcuts import render, redirect
from .models import Game, Publisher
from .forms import ReviewForm
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
  fields= ['name', 'type', 'description']
class GameUpdate(UpdateView):
  model= Game
  fields= '__all__'
class GameDelete(DeleteView):
  model=Game
  success_url='/games/'
class GameDetail(DetailView):
  model=Game
  def get_context_data(self, **kwargs):
    review_form = ReviewForm()
    context = super().get_context_data(**kwargs)
    context["review_form"] = review_form
    return context
def add_review(request, pk):
  form=ReviewForm(request.POST)
  if form.is_valid():
    new_review=form.save(commit=False)
    new_review.game_id=pk
    new_review.save()
  return redirect('games_detail', pk=pk)

# def games_index(request):
#   games=Game.objects.all()
#   return render(request, 'games/index.html', {'games': games})
# def games_detail(request, game_id):
#   game = Game.objects.get(id=game_id)
#   return render(request, 'games/detail.html', { 'game': game })
class PublisherList(ListView):
  model = Publisher

class PublisherDetail(DetailView):
  model = Publisher

class PublisherCreate(CreateView):
  model = Publisher
  fields = '__all__'

class PublisherUpdate(UpdateView):
  model = Publisher
  fields = ['name']

class PublisherDelete(DeleteView):
  model = Publisher
  success_url = '/publisher'

def assoc_publisher(request, cat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Game.objects.get(id=cat_id).publisher.add(toy_id)
  return redirect('detail', cat_id=cat_id)

def remove_publisher(request, cat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Game.objects.get(id=cat_id).publisher.remove(toy_id)
  return redirect('detail', cat_id=cat_id)