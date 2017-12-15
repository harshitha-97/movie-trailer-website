import fresh_tomatoes
import media
Toy_story_4=media.Movie(
    "Toy Story 4",
    '''Woody (Tom Hanks) reunites with Bo Peep.''',
    "http://www.gstatic.com/tv/thumb/movieposters/12004128/p12004128_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=QW0sjQFpXTU")

Fantastic_beasts_and_where_to_find_them = media.Movie(
    "Fantastic beasts and where to find them",
    '''The year is 1926, and Newt Scamander (Eddie Redmayne) has
    just completed a global excursion to find and
    document an extraordinary array of magical creatures.''',
    "http://prodimage.images-bn.com/pimages/0883929541003_p0_v2_s1200x630.jpg",
    "https://www.youtube.com/watch?v=Vso5o11LuGU")

Guardians_of_Galaxy_vol_2 = media.Movie(
    "Guardians of Galaxy Vol 2",
    '''Peter Quill and his fellow Guardians are hired
    by a powerful alien race, the Sovereign, to
    protect their precious batteries from invaders.''',
    "https://vignette1.wikia.nocookie.net/marvelcinematicuniverse/images/b/b1/GOTG_Vol.2_OST.jpg/revision/latest?cb=20170421210218", # noqa
    "https://www.youtube.com/watch?v=pr7tDrwQ3t8")

Despicable_Me_3 = media.Movie(
    "Despicable Me 3",
    '''The mischievous Minions hope that Gru will return to a life of crime after the new boss of
    the Anti-Villain League fires him. Instead, Gru decides to remain retired and travel to Freedonia to
    meet his long-lost twin brother for the first time. The reunited siblings soon find themselves in an uneasy
    alliance to take down the elusive Balthazar Bratt, a former 1980s child star who seeks revenge against the world.''',
    "https://doubletoasted.com/wp-content/uploads/2017/07/depicable-me-3-1.jpg",
    "https://www.youtube.com/watch?v=6DBi41reeF0")

Kingsman_The_Golden_Circle=media.Movie(
    "Kingsman: The Golden Circle",
    '''With their headquarters destroyed and the world held hostage, members of Kingsman find
    new allies when they discover a spy organization in the United States known as Statesman. In an adventure
    that tests their strength and wits, the elite secret agents from both sides of the pond band together to battle a
    ruthless enemy and save the day, something that's becoming a bit of a habit for Eggsy.''',
    "https://upload.wikimedia.org/wikipedia/en/7/73/Kingsman_The_Golden_Circle.jpg",
    "https://www.youtube.com/watch?v=0fvqnGmr9S8")

The_Notebook=media.Movie(
    "The Notebook",
    '''Duke reads the story of Allie and Noah, two lovers who were separated by fate, to
    Ms. Hamilton, an old woman who suffers from Alzheimer's, on a daily basis out of his notebook.''',
    "http://nicholassparks.com/wp-content/uploads/2013/07/200406-the-notebook.jpeg",
    "https://www.youtube.com/watch?v=yDJIcYE32NU")

movies=[Toy_story_4,
        Fantastic_beasts_and_where_to_find_them,
        Guardians_of_Galaxy_vol_2,
        Despicable_Me_3,
        Kingsman_The_Golden_Circle,
        The_Notebook]
fresh_tomatoes.open_movies_page(movies)


