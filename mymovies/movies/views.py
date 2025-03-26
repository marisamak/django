# movies\views.py

from django.shortcuts import get_object_or_404, render,  redirect
from .models import Movie, Comment
from .forms import CommentForm, RegisterForm
from django.contrib.auth import login

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    print(f"Функция `movie_detail` вызвана для фильма ID {movie_id}")
    movie = get_object_or_404(Movie, id=movie_id)
    comments = movie.comments.all()
    form = CommentForm()  # Форма создаётся всегда

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.movie = movie
                new_comment.author = request.user
                new_comment.save()
                form = CommentForm()  # Очищаем форму после отправки
        else:
            form.add_error(None, "Вы должны войти в систему, чтобы оставить комментарий.")

    print(f"Форма передаётся в шаблон: {form}")

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'comments': comments,
        'form': form,  # Форма передаётся в шаблон!
    })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('movie_list')  # Перенаправление на список фильмов
    else:
        form = RegisterForm()
    return render(request, 'movies/register.html', {'form': form})