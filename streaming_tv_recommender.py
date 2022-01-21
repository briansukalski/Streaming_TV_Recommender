#Setting up the TV show class
class Series():
    def __init__(self, name, streaming_service, genres, traits, story_style, content_rating, number_of_episodes, imdb_rating, metacritic_rating, imdb_synopsis, review=""):
        self.name = name
        self.streaming_service = streaming_service
        self.genres = genres
        self.traits = traits
        self.story_style = story_style
        self.content_rating = content_rating
        self.number_of_episodes = number_of_episodes
        self.imdb_rating = imdb_rating
        self.metacritic_rating = metacritic_rating
        self.imdb_synopsis = imdb_synopsis
        self.review = review

tv_shows = []
#Function for turning a list of values into a Series instance and adding it to the tv_shows list
def add_show(name, streaming_service, genres, traits, story_style, content_rating, number_of_episodes, imdb_rating, metacritic_rating, imdb_synopsis, review=""):
    new_show = Series(name, streaming_service, genres, traits, story_style, content_rating, number_of_episodes, imdb_rating, metacritic_rating, imdb_synopsis, review)

    tv_shows.append(new_show)

#Setting up lists for streaming service, genres, and attributes
streaming_services = ["Netflix", "Hulu", "Disney+", "Peacock", "HBO Max", "Paramount+", "Amazon Prime Video", "Apple TV Plus"]
genres = ["Drama", "Comedy", "Action", "Reality", "Game Show", "Horror", "Adventure", "Crime", "Fantasy", "Musical", "Romance", "Science Fiction", "Thriller", "War", "Western", "Historical", "Biographical", "Documentary", "Superhero"]
traits = ["Satirical", "Meta", "Dark", "Witty", "Dry", "Wacky", "Irreverent", "Dramatic", "Mind-Bending", "Cynical", "Heartfelt", "Violent", "Gritty", "Steamy", "Challenging", "Easy-to-Watch", "Uncomfortable", "Provocative", "Epic", "Competitive", "Feel-Good", "Nostalgic", "Psychological", "Mysterious", "Political", "Dystopian", "Non-English", "Animated", "For Kids"]
story_styles = ["Serialized", "Mixed", "Episodic"]
content_ratings = ["Y", "Y7", "G", "PG", "14", "MA"]

#Hulu Shows
add_show("Only Murders in the Building", "Hulu", ["Comedy", "Crime"], ["Mysterious", "Witty", "Meta"], "Serialized", "MA", 10, 8.1, 76, "Three strangers who share an obsession with true crime suddenly find themselves caught up in one.")
add_show("King of the Hill", "Hulu", ["Comedy"], ["Dry", "Witty", "Satirical", "Animated"], "Episodic", "14", 259, 7.3, 70, "A straight-laced propane salesman in Arlen, Texas tries to deal with the wacky antics of his family and friends, while also trying to keep his son in line.")
add_show("The Eric Andre Show", "Hulu", ["Comedy"], ["Wacky", "Irreverent", "Uncomfortable"], "Episodic", "MA", 40, 8.6, 79, "Eric Andre tries to host a talk show in a bizarre environment, where he is sometimes the player of pranks and sometimes the victim.")
add_show("Scrubs", "Hulu", ["Comedy"], ["Witty", "Heartfelt", "Wacky", "Meta"], "Mixed", "14", 182, 8.3, 74, "In the unreal world of Sacred Heart Hospital, intern John \"J.D.\" Dorian learns the ways of medicine, friendship and life.")
add_show("Brooklyn Nine-Nine", "Hulu", ["Comedy"], ["Witty", "Heartfelt", "Easy-to-Watch"], "Mixed", "14", 147, 8.4, 73, "Comedy series following the exploits of Det. Jake Peralta and his diverse, lovable colleagues as they police the NYPD's 99th Precinct.")
add_show("It's Always Sunny in Philadelphia", "Hulu", ["Comedy"], ["Dark", "Witty", "Irreverent", "Cynical", "Meta", "Uncomfortable"], "Mixed", "MA", 154, 8.8, 71, "Five friends with big egos and small brains are the proprietors of an Irish pub in Philadelphia.")

#Netflix Shows
add_show("Seinfeld", "Netflix", ["Comedy"], ["Witty", "Irreverent", "Cynical"], "Mixed", "PG", 171, 8.8, 79, "The continuing misadventures of neurotic New York City stand-up comedian Jerry Seinfeld and his equally neurotic New York City friends.")
add_show("I Think You Should Leave with Tim Robinson", "Netflix", ["Comedy"], ["Witty", "Wacky", "Irreverent", "Uncomfortable"], "Episodic", "MA", 12, 7.9, 83, "In this new sketch show, Tim Robinson and guests spend each segment driving someone to the point of needing -- or desperately wanting -- to leave.")
add_show("Arrested Development", "Netflix", ["Comedy"], ["Witty", "Dry", "Wacky", "Irreverent"], "Mixed", "MA", 91, 8.7, 78, "Level-headed son Michael Bluth takes over family affairs after his father is imprisoned. But the rest of his spoiled, dysfunctional family are making his job unbearable.")
add_show("Community", "Netflix", ["Comedy"], ["Witty", "Irreverent", "Wacky", "Meta"], "Mixed", "14", 109, 8.5, 74, "A suspended lawyer is forced to enroll in a community college with an eccentric staff and student body.")
add_show("Cobra Kai", "Netflix", ["Comedy", "Drama", "Action"], ["Dramatic", "Irreverent", "Heartfelt", "Nostalgic"], "Serialized", "14", 40, 8.6, 70, "Decades after their 1984 All Valley Karate Tournament bout, a middle-aged Daniel LaRusso and Johnny Lawrence find themselves martial-arts rivals again.")
add_show("Breaking Bad", "Netflix", ["Drama", "Crime", "Thriller", "Western"], ["Dark", "Violent", "Gritty", "Challenging"], "Serialized", "MA", 62, 9.4, 87, "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.")
add_show("Avatar: The Last Airbender", "Netflix", ["Adventure", "Fantasy"], ["Heartfelt", "Epic", "Animated", "For Kids"], "Serialized", "Y7", 54, 9.3, 84, "In a war-torn world of elemental magic, a young boy reawakens to undertake a dangerous mystic quest to fulfill his destiny as the Avatar, and bring peace to the world.")
add_show("Stranger Things", "Netflix", ["Adventure", "Science Fiction", "Horror"], ["Heartfelt", "Nostalgic", "Dark"], "Serialized", "14", 25, 8.7, 75, "When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces in order to get him back.")
add_show("The Last Dance", "Netflix", ["Documentary", "Biographical"], ["Nostalgic"], "Serialized", "MA", 10, 9.1, 90, "Charting the rise of the 1990's Chicago Bulls, led by Michael Jordan, one of the most notable dynasties in sports history.")
add_show("Making a Murderer", "Netflix", ["Documentary", "Crime"], ["Dark", "Provocative", "Dramatic"], "Serialized", "14", 20, 8.5, 77, "Filmed over a 10-year period, Steven Avery, a DNA exoneree who, while in the midst of exposing corruption in local law enforcement, finds himself the prime suspect in a grisly new crime.")
add_show("Too Hot to Handle", "Netflix", ["Reality"], ["Dramatic", "Steamy", "Provocative", "Competitive", "Easy-to-Watch"], "Serialized", "MA", 29, 4.6, 43, "On the shores of paradise, gorgeous singles meet and mingle. But there's a twist. To win a $100,000 grand prize, they'll have to give up sex.")
add_show("The Witcher", "Netflix", ["Fantasy", "Drama", "Action"], ["Dark", "Epic", "Violent", "Gritty"], "Serialized", "MA", 16, 8.2, 62, "Geralt of Rivia, a solitary monster hunter, struggles to find his place in a world where people often prove more wicked than beasts.")
add_show("Bojack Horseman", "Netflix", ["Comedy", "Drama"], ["Dark", "Dry", "Irreverent", "Animated", "Witty", "Provocative", "Challenging"], "Serialized", "MA", 76, 8.7, 82, "BoJack Horseman was the star of the hit television show \"Horsin' Around\" in the '80s and '90s, but now he's washed up, living in Hollywood, complaining about everything, and wearing colorful sweaters.")
add_show("Love, Death & Robots", "Netflix", ["Science Fiction", "Thriller"], ["Dark", "Violent", "Animated", "Mind-Bending", "Dystopian", "Challenging"], "Episodic", "MA", 26, 8.5, 65, "A collection of animated short stories that span various genres including science fiction, fantasy, horror and comedy.")
add_show("The Last Kingdom", "Netflix", ["Drama", "Historical", "Fantasy", "Action"], ["Dark", "Gritty", "Violent", "Epic"], "Serialized", "MA", 36, 8.4, 78, "As Alfred the Great defends his kingdom from Norse invaders, Uhtred--born a Saxon but raised by Vikings--seeks to claim his ancestral birthright.")
add_show("Squid Game", "Netflix", ["Drama", "Thriller"], ["Dark", "Gritty", "Political", "Dystopian", "Non-English"], "Serialized", "MA", 9, 8.0, 69, "Hundreds of cash-strapped players accept a strange invitation to compete in children's games. Inside, a tempting prize awaits with deadly high stakes. A survival game that has a whopping 45.6 billion-won prize at stake.")
add_show("Bodyguard", "Netflix", ["Drama", "Thriller", "Crime"], ["Gritty", "Dramatic", "Steamy"], "Serialized", "MA", 6, 8.1, 79, "A contemporary thriller featuring the Royalty and Specialist Protection Branch of London's Metropolitan Police Service.")
add_show("The Blacklist", "Netflix", ["Crime", "Thriller"], ["Mysterious", "Psychological"], "Mixed", "14", 174, 8.0, 74, "A new FBI profiler, Elizabeth Keen, has her entire life uprooted when a mysterious criminal, Raymond Reddington, who has eluded capture for decades, turns himself in and insists on speaking only to her.")
add_show("The Great British Baking Show", "Netflix", ["Reality"], ["Competitive", "Feel-Good", "Easy-to-Watch"], "Serialized", "14", 50, 8.6, 82, "Bakers attempt three challenges each week trying to impress the judges enough to go through to the next round and eventually are crowned Britain's best amateur baker.")
add_show("Midnight Mass", "Netflix", ["Drama", "Horror"], ["Dark", "Psychological", "Provocative", "Mysterious", "Challenging"], "Serialized", "MA", 7, 7.7, 75, "An isolated island community experiences miraculous events - and frightening omens - after the arrival of a charismatic, mysterious young priest.")

