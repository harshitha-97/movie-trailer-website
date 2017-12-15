# **Movie Trailer Website**

##Introduction:
The Movie Trailer Website project consists of **_server-side code_** to store a list of movies titles, along with its respective image and movie trailers. The data should be served as a web page allowing visitors to review the movies and watch the trailers.

##Example:

I want this **Toy Story 4** title,poster and movie trailer to be displayed.
So i create a class of movie objects namely
-movie_title
-story_line
-poster_image
-youtube_url_link

```Python

class Movie():

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

   def show_trailer(self):
      webbrowser.open(self.trailer_youtube_url)   

  ```

and to instantiate movie objects we are calling by constructor **media.Movie()** for that class as follows of your movie choice

  ```Python

  Toy_Story_4=media.Movie(
    "Toy Story 4",
    '''Woody (Tom Hanks) reunites with Bo Peep.''',
    "http://www.gstatic.com/tv/thumb/movieposters/12004128/p12004128_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=QW0sjQFpXTU")

  ```

and group all the instances together in a list perhaps like this

```Python

movies=[Toy_story_4,
        Fantastic_beasts_and_where_to_find_them,
        Guardians_of_Galaxy_vol_2,
        Despicable_Me_3,
        Kingsman_The_Golden_Circle,
        The_Notebook]
```

##Required Library:

_Python 2.7_ version is needed for coding.

##Contents

-entertainment_center.py
-fresh_tomatoes.py
-media.py

```

*.py

```

##Operating Instruction:

To generate a website that displays these movies, there should be a function called open_movies_page() that takes in one argument, which is a list of movies, and creates an HTML file which will display all of your favorite movies. And that function resides in _fresh_tomatoes.py_ file. So it is a  must to run your website.

```Python

fresh_tomatoes.open_movies_page(movies)

```
And the website appears in HTML format.

##License:

It is a public domain work and feel free to do whatever you want to do with it.
