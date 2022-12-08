from flask import Flask, request, render_template
from utils import get_movie_by_title, get_movie_year_to_year, get_children_movie, get_family_movie, get_adult_movie, get_movie_by_genre

app = Flask(__name__)


@app.get('/movie/title')
def page_movie_by_title():
    title = request.args.get('title')
    movie = get_movie_by_title(title)
    return render_template('page_movie_by_title.html', movie=movie)


@app.get('/search/movie')
def page_search_movie_by_title():
    return render_template('page_search_movie_by_title.html')


@app.get('/movie/year_to_year')
def page_movie_year_to_year():
    from_year = int(request.args.get('from_year'))
    to_year = int(request.args.get('to_year'))
    movie = get_movie_year_to_year(from_year, to_year)
    return render_template('page_movie_year_to_year.html', movie=movie)


@app.get('/search/movie/year_to_year')
def page_search_movie_yea_to_year():
    return render_template('page_search_movie_year_to_year.html')


@app.get('/rating/children')
def page_children_rating():
    movie = get_children_movie()
    return render_template('page_rating.html', movie=movie)


@app.get('/rating/family')
def page_family_rating():
    movie = get_family_movie()
    return render_template('page_rating.html', movie=movie)


@app.get('/rating/adult')
def page_adult_rating():
    movie = get_adult_movie()
    return render_template('page_rating.html', movie=movie)


@app.get('/genre/genre')
def page_genre():
    genre = request.args.get('genre')
    movie = get_movie_by_genre(genre)
    return render_template('page_genre.html', movie=movie)


@app.get('/search/genre')
def page_search_genre():
    return render_template('page_search_genre.html')


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000)
