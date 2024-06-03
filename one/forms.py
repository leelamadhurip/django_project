from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

from django import forms
from .models import MovieList, Movie

class MovieListForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ['name', 'is_public']

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'imdb_id']
        widgets = {
            'title': forms.HiddenInput(),
            'imdb_id': forms.HiddenInput(),
        }

from django import forms
from .models import MovieList, Movie

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'imdb_id']
