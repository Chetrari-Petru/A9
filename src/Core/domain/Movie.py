import random
class Movie:
    __movie_id = None
    title = None
    description = None
    genre = None
    def __init__(self, title, description, genre, id):
        """
        Creates a Movie Object
        :param title: The title of the movie
        :param description: The description of the movie
        :param genre: The genre of the movie
        :param id: The given id
        """
        self.__movie_id = int(id)
        self.title = title
        self.description = description
        self.genre = genre

    def __dict__(self):
        return {"id": self.__movie_id, "title": self.title, "description": self.description, "genre": self.genre}

    def __repr__(self):
        return str(self.__dict__())+"\n"

    def get_id(self):
        return self.__movie_id

    def change_field(self, field, value):
        if field == "title":
            self.title = value
        if field == "description":
            self.description = value
        if field == "genre":
            self.genre = value


    @staticmethod
    def sample(number_of_samples):
        ls = []
        _rentals = movies.copy()
        for i in range(number_of_samples):
            obj = _rentals.pop(random.randint(0, len(_rentals) - 1))
            ls[obj.get_id()] = obj

        return ls

movies = [
    Movie("Hidden Whisper", "An epic adventure through unknown lands.", "Mystery", 1),
    Movie("Furious Legacy", "A heartwarming story of friendship and courage.", "Thriller", 2),
    Movie("Dark Revenge", "A story of hope in the face of darkness.", "Mystery", 3),
    Movie("Shattered Legacy", "A journey to discover hidden truths.", "Mystery", 4),
    Movie("Shattered Horizon", "A fight for survival against all odds.", "Sci-Fi", 5),
    Movie("Silent Dream", "An unforgettable quest for redemption.", "Drama", 6),
    Movie("Eternal Whisper", "A tale of love and betrayal.", "Romance", 7),
    Movie("Lost Journey", "A world where nothing is as it seems.", "Adventure", 8),
    Movie("Golden Hunter", "An emotional rollercoaster with shocking twists.", "Action", 9),
    Movie("Hidden Curse", "The ultimate battle between good and evil.", "Fantasy", 10),
    Movie("Broken Whisper", "An epic adventure through unknown lands.", "Mystery", 11),
    Movie("Last Secret", "A heartwarming story of friendship and courage.", "Mystery", 12),
    Movie("Dark Shadow", "A story of hope in the face of darkness.", "Thriller", 13),
    Movie("Golden Legacy", "A journey to discover hidden truths.", "Adventure", 14),
    Movie("Shattered Hunter", "A fight for survival against all odds.", "Action", 15),
    Movie("Lost Horizon", "An unforgettable quest for redemption.", "Sci-Fi", 16),
    Movie("Silent Curse", "A tale of love and betrayal.", "Horror", 17),
    Movie("Furious Shadow", "A world where nothing is as it seems.", "Thriller", 18),
    Movie("Broken Hunter", "An emotional rollercoaster with shocking twists.", "Adventure", 19),
    Movie("Last Journey", "The ultimate battle between good and evil.", "Adventure", 20),
    Movie("Hidden Secret", "An epic adventure through unknown lands.", "Mystery", 21),
    Movie("Golden Shadow", "A heartwarming story of friendship and courage.", "Drama", 22),
    Movie("Dark Whisper", "A story of hope in the face of darkness.", "Horror", 23),
    Movie("Eternal Legacy", "A journey to discover hidden truths.", "Drama", 24),
    Movie("Shattered Secret", "A fight for survival against all odds.", "Sci-Fi", 25),
    Movie("Lost Curse", "An unforgettable quest for redemption.", "Fantasy", 26),
    Movie("Silent Horizon", "A tale of love and betrayal.", "Sci-Fi", 27),
    Movie("Furious Curse", "A world where nothing is as it seems.", "Horror", 28),
    Movie("Dark Dream", "An emotional rollercoaster with shocking twists.", "Fantasy", 29),
    Movie("Broken Revenge", "The ultimate battle between good and evil.", "Action", 30),
    Movie("Last Shadow", "An epic adventure through unknown lands.", "Thriller", 31),
    Movie("Golden Secret", "A heartwarming story of friendship and courage.", "Drama", 32),
    Movie("Hidden Hunter", "A story of hope in the face of darkness.", "Adventure", 33),
    Movie("Furious Whisper", "A journey to discover hidden truths.", "Mystery", 34),
    Movie("Shattered Curse", "A fight for survival against all odds.", "Horror", 35),
    Movie("Silent Secret", "An unforgettable quest for redemption.", "Mystery", 36),
    Movie("Lost Hunter", "A tale of love and betrayal.", "Action", 37),
    Movie("Eternal Journey", "A world where nothing is as it seems.", "Adventure", 38),
    Movie("Dark Curse", "An emotional rollercoaster with shocking twists.", "Horror", 39),
    Movie("Shattered Whisper", "The ultimate battle between good and evil.", "Fantasy", 40),
    Movie("Broken Shadow", "An epic adventure through unknown lands.", "Thriller", 41),
    Movie("Golden Whisper", "A heartwarming story of friendship and courage.", "Drama", 42),
    Movie("Hidden Journey", "A story of hope in the face of darkness.", "Adventure", 43),
    Movie("Furious Secret", "A journey to discover hidden truths.", "Mystery", 44),
    Movie("Silent Curse", "A fight for survival against all odds.", "Horror", 45),
    Movie("Lost Dream", "An unforgettable quest for redemption.", "Fantasy", 46),
    Movie("Shattered Hunter", "A tale of love and betrayal.", "Action", 47),
    Movie("Eternal Secret", "A world where nothing is as it seems.", "Drama", 48),
    Movie("Dark Horizon", "An emotional rollercoaster with shocking twists.", "Sci-Fi", 49),
    Movie("Last Whisper", "The ultimate battle between good and evil.", "Fantasy", 50)
]
