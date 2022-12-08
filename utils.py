import sqlite3


def get_movie_by_title(title):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = "select title, country, release_year, listed_in, description from netflix where title = ? order by date_added desc limit 1"
        cursor.execute(sqlite_query, (title,))
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {
            'title': result[0].get('title'),
            'country': result[0].get('country'),
            'release_year': result[0].get('release_year'),
            'genre': result[0].get('listed_in'),
            'description': result[0].get('description').strip()
        }


def get_movie_year_to_year(from_year, to_year):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = "select title, release_year from netflix where release_year between ? and ?"
        cursor.execute(sqlite_query, (from_year, to_year))
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return result


def get_children_movie():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = "select title, rating, description from netflix where rating = 'G'"
        cursor.execute(sqlite_query)
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        list_movie = []
        for row in result:
            list_movie.append({
                'title': row.get('title'),
                'rating': row.get('rating'),
                'description': row.get('description').strip()
            })
        return list_movie


def get_family_movie():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = "select title, rating, description from netflix where rating in ('G', 'PG', 'PG-13')"
        cursor.execute(sqlite_query)
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        list_movie = []
        for row in result:
            list_movie.append({
                'title': row.get('title'),
                'rating': row.get('rating'),
                'description': row.get('description').strip()
            })
        return list_movie


def get_adult_movie():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = "select title, rating, description from netflix where rating in ('R', 'NC-17')"
        cursor.execute(sqlite_query)
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        list_movie = []
        for row in result:
            list_movie.append({
                'title': row.get('title'),
                'rating': row.get('rating'),
                'description': row.get('description').strip()
            })
        return list_movie


def get_movie_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = "select title, description from netflix where listed_in like ? order by date_added desc limit 10"
        cursor.execute(sqlite_query, (f'%{genre}%',))
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        list_movie = []
        for row in result:
            list_movie.append({
                'title': row.get('title'),
                'description': row.get('description').strip()
            })
        return list_movie


def get_movie_by_type_release_year_genre(type_, release_year, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = "select title, description from netflix where type = ? and release_year = ? and listed_in like ?"
        cursor.execute(sqlite_query, (type_, release_year, f'%{genre}%'))
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        list_movie = []
        for row in result:
            list_movie.append({
                'title': row.get('title'),
                'description': row.get('description').strip()
            })
        return list_movie
