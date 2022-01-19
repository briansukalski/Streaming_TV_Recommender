#Setting up the TV show class
class Series():
    def __init__(self, name, streaming_service, genres, traits, content_rating, number_of_episodes, imdb_rating, metacritic_rating, synopsis, review=""):
        self.name = name
        self.streaming_service = streaming_service
        self.genres = genres
        self.traits = traits
        self.content_rating = content_rating
        self.number_of_episodes = number_of_episodes
        self.imdb_rating = imdb_rating
        self.metacritic_rating = metacritic_rating
        self.description = synopsis
        self.review = review
    
#Setting up lists for streaming service, genres, and attributes
streaming_services = ["Netflix", "Hulu", "Disney+", "Peacock", "HBO Max", "Paramount+", "Amazon Prime Video", "Apple TV Plus"]
genres = ["Drama", "Comedy", "Mystery", "Action", "Reality", "Game Show", "Horror", "Adventure", "Crime", "Fantasy", "Musical", "Romance", "Science Fiction", "Thriller", "War", "Western", "Historical", "Biographical", "Documentary"]
attributes = ["Satirical", "Slapstick", "Dark", "Witty", "Irreverent", "Offensive", "Profane", "Sweet", "Cynical", "Hopeful", "Violent", "Adult", "Epic", "Loud", "Competitive", "Feel-Good", "Psychological", "Political", "Ensemble-Driven", "Character Study", "Serial", "Episodic", "Female-Led", "Racial Minority-Led", "Non-English", "Animated", "For Kids", "Mature"]
content_ratings = ["Y", "Y7", "G", "PG", "14", "MA"]