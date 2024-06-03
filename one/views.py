from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from django.http import JsonResponse
from .models import MovieList, Movie
from .forms import MovieListForm, AddMovieForm
from django.views.decorators.http import require_POST
from django.contrib import messages

def home(request):
    context = {
        'signup_url': reverse('signup'),
        'signin_url': reverse('signin'),
        'signout_url': reverse('signout'),
        'search_url': reverse('search'),
    }
    if request.user.is_authenticated:
        context['lists'] = MovieList.objects.filter(user=request.user)
    return render(request, "one/index.html", context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'one/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'one/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')

@login_required
def search_movies(request):
    query = request.GET.get('query')
    movies = []
    if query:
        url = f"http://www.omdbapi.com/?apikey={settings.OMDB_API_KEY}&s={query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('Search'):
                movies = data['Search']
    
    movie_lists = MovieList.objects.filter(user=request.user)
    add_movie_form = AddMovieForm()
    create_movie_list_form = MovieListForm()

    return render(request, 'one/search.html', {
        'movies': movies,
        'query': query,
        'movie_lists': movie_lists,
        'add_movie_form': add_movie_form,
        'create_movie_list_form': create_movie_list_form,
    })

@require_POST
@login_required
def add_movie_to_list(request, imdb_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        movie_list_id = request.POST.get('movie_list')
        title = request.POST.get('title')
        movie_list = get_object_or_404(MovieList, id=movie_list_id, user=request.user)
        Movie.objects.create(movie_list=movie_list, title=title, imdb_id=imdb_id)
        return JsonResponse({'status': 'success'})
    return redirect('home')

@require_POST
@login_required
def create_movie_list(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = MovieListForm(request.POST)
        if form.is_valid():
            movie_list = form.save(commit=False)
            movie_list.user = request.user
            movie_list.save()
            return JsonResponse({'status': 'success'})
    return redirect('home')


@login_required
def movie_lists(request):
    lists = MovieList.objects.filter(user=request.user)
    return render(request, 'one/movie_lists.html', {'lists': lists})

@login_required
def create_movie_list_and_add(request):
    if request.method == 'POST':
        form = MovieListForm(request.POST)
        if form.is_valid():
            movie_list = form.save(commit=False)
            movie_list.user = request.user
            movie_list.save()
            return redirect('movie_lists')
    else:
        form = MovieListForm()
    return render(request, 'one/create_movie_list.html', {'form': form})

@login_required
def add_movie(request, list_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        imdb_id = request.POST.get('imdb_id')
        movie_list = MovieList.objects.get(id=list_id, user=request.user)
        Movie.objects.create(movie_list=movie_list, title=title, imdb_id=imdb_id)
        return redirect('movie_lists')
    return render(request, 'one/add_movie.html', {'list_id': list_id})

from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import MovieList

@require_POST
@login_required
def delete_movie_list(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    movie_list.delete()
    return redirect('home')

@require_POST
@login_required
def toggle_privacy(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    movie_list.is_public = not movie_list.is_public
    movie_list.save()
    return redirect('home')

@login_required
def view_public_list(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, is_public=True)
    return render(request, 'one/view_public_list.html', {'movie_list': movie_list})
