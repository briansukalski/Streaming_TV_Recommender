import maxheap
import scrollprint

#Setting up the TV show class
class Series():
    def __init__(self, name, streaming_service, genres, traits, story_style, content_rating, number_of_episodes, imdb_rating, metacritic_rating, imdb_synopsis):
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
        self.score = 0

    #Output representation of Series
    def __repr__(self):
        #1st line: series name
        str_repr = f"\n{self.name}\n\n"
        #2nd line: streaming service
        str_repr += f"Streaming on {self.streaming_service}\n\nGenre(s): "
        #3rd line: loops through series genres and appends each to repr, comma-separated
        for genre in self.genres:
            str_repr += genre + ", "
        #Removes comma from end of last genre and sets more line breaks
        str_repr = str_repr[:-2] + "\n\n"
        #4th line: loops through series traits and appends each to repr, comma_separated
        str_repr += "Traits: "
        for trait in self.traits:
            str_repr += trait + ", "
        #Removes comma from end of last genre and sets more line breaks
        str_repr = str_repr[:-2] + "\n\n"
        #5th line: story style, content rating, number of episodes
        str_repr += f"Story Style: {self.story_style} | Content Rating: TV {self.content_rating} | Number of Episodes: {self.number_of_episodes}\n\n"
        #6th line: IMDB rating and Metacritic rating
        str_repr += f"IMDB User Score (Out of 10): {self.imdb_rating} | Metacritic Critic Score (Out of 100): {self.metacritic_rating}\n\n"
        #7th and final line: Imdb synopsis
        str_repr += f"{self.imdb_synopsis}\n\n_________________________\n"

        return str_repr

#Dictionary for catalogs from each different streaming services
tv_shows = {}

#Function for turning a list of values into a Series instance and adding it to the tv_shows dictionary under its streaming service
def add_show(name, streaming_service, genres, traits, story_style, content_rating, number_of_episodes, imdb_rating, metacritic_rating, imdb_synopsis):
    new_show = Series(name, streaming_service, genres, traits, story_style, content_rating, number_of_episodes, imdb_rating, metacritic_rating, imdb_synopsis)

    tv_shows[new_show.streaming_service].append(new_show)



#Setting up lists for streaming service, genres, and attributes
streaming_services = ["Netflix", "Hulu", "Disney+", "Peacock", "HBO Max", "Paramount+", "Amazon Prime", "Apple TV+"]
genres = ["Drama", "Comedy", "Action", "Reality", "Game Show", "Horror", "Adventure", "Crime", "Fantasy", "Musical", "Romance", "Science Fiction", "Thriller", "War", "Western", "Historical", "Biographical", "Documentary", "Superhero"]
traits = ["Satirical", "Meta", "Dark", "Witty", "Dry", "Wacky", "Irreverent", "Dramatic", "Mind-Bending", "Cynical", "Heartfelt", "Violent", "Gritty", "Steamy", "Complex", "Easy-to-Watch", "Uncomfortable", "Provocative", "Epic", "Competitive", "Feel-Good", "Nostalgic", "Emotional", "Psychological", "Mysterious", "Political", "Dystopian", "Non-English", "Animated", "Coming-of-Age", "For Kids"]
story_styles = ["Serialized", "Seasonal", "Mixed", "Episodic"]
content_ratings = {"Y": 1, "G": 2, "Y7": 3, "PG": 4, "14": 5, "MA": 6}

#Setting up dictionary for tv shows, sorted by streaming service
for service in streaming_services:
    tv_shows[service] = []

#Amazon Prime Shows
add_show("Psych", "Amazon Prime", ["Crime", "Comedy"], ["Witty", "Easy-to-Watch"], "Episodic", "14", 120, 8.3, 60, "A novice sleuth is hired by the Police after he cons them into thinking he has psychic powers which help solve crimes. With the assistance of his reluctant best friend, the duo take on a series of complicated cases.")
add_show("Fleabag", "Amazon Prime", ["Comedy"], ["Witty", "Irreverent", "Provocative"], "Serialized", "MA", 12, 8.7, 92, "A comedy series adapted from the award-winning play about a young woman trying to cope with life in London whilst coming to terms with a recent tragedy.")
add_show("The Wheel of Time", "Amazon Prime", ["Fantasy", "Drama"], ["Dark", "Violent", "Gritty"], "Serialized", "MA", 8, 7.2, 55, "Set in a high fantasy world where magic exists, but only some can access it, a woman named Moiraine crosses paths with five young men and women. This sparks a dangerous, world-spanning journey. Based on the book series by Robert Jordan.")
add_show("Tom Clancy's Jack Ryan", "Amazon Prime", ["Action", "Adventure"], ["Witty", "Dramatic"], "Serialized", "MA", 16, 8.1, 64, "An up-and-coming CIA analyst, Jack Ryan, is thrust into a dangerous field assignment as he uncovers a pattern in terrorist communication that launches him into the center of a dangerous gambit.")
add_show("The Boys", "Amazon Prime", ["Superhero"], ["Dark", "Violent", "Cynical", "Satirical", "Provocative", "Dystopian"], "Serialized", "MA", 16, 8.7, 77, "A group of vigilantes set out to take down corrupt superheroes who abuse their superpowers.")

#Apple TV+
add_show("See", "Apple TV+", ["Drama", "Action", "Fantasy"], ["Epic", "Violent", "Gritty", "Dystopian"], "Serialized", "MA", 16, 7.7, 40, "Far in a dystopian future, the human race has lost the sense of sight, and society has had to find new ways to interact, build, hunt, and to survive. All of that is challenged when a set of twins are born with sight.")
add_show("The Morning Show", "Apple TV+", ["Drama"], ["Dramatic", "Provocative", "Political"], "Serialized", "MA", 20, 8.3, 61, "An inside look at the lives of the people who help America wake up in the morning, exploring the unique challenges faced by the men and women who carry out this daily televised ritual.")
add_show("Ted Lasso", "Apple TV+", ["Comedy"], ["Witty", "Heartfelt", "Feel-Good", "Emotional"], "Serialized", "MA", 22, 8.8, 79, "American college football coach Ted Lasso heads to London to manage AFC Richmond, a struggling English Premier League soccer team.")
add_show("Mythic Quest", "Apple TV+", ["Comedy"], ["Witty", "Irreverent"], "Serialized", "MA", 20, 7.8, 73, "The owner of a successful video game design company and his troubled staff struggle to keep their hit game 'Mythic Quest' on top.")
add_show("Foundation", "Apple TV+", ["Science Fiction", "Drama"], ["Complex", "Mind-Bending", "Epic"], "Serialized", "14", 10, 7.4, 62, "A complex saga of humans scattered on planets throughout the galaxy all living under the rule of the Galactic Empire.")

#Paramount+ Shows
add_show("Star Trek: Discovery", "Paramount+", ["Adventure", "Science Fiction"], ["Epic", "Complex", "Dramatic"], "Mixed", "14", 49, 7.1, 73, "Ten years before Kirk, Spock, and the Enterprise, the USS Discovery discovers new worlds and lifeforms as one Starfleet officer learns to understand all things alien.")
add_show("Seal Team", "Paramount+", ["Drama", "War"], ["Dramatic", "Violent", "Gritty"], "Serialized", "14", 93, 7.7, 57, "The lives of the elite Navy SEALs as they train, plan and execute the most dangerous, high-stakes missions the United States of America can ask.")
add_show("The Amazing Race", "Paramount+", ["Reality", "Adventure"], ["Competitive"], "Seasonal", "PG", 343, 7.6, 72, "Multiple teams race around the globe for $1,000,000 to 'amazing' locations.")
add_show("Fairly Oddparents", "Paramount+", ["Comedy"], ["Wacky", "Animated", "For Kids"], "Episodic", "Y7", 172, 7.2, 60, "After being tortured and humiliated by his babysitter, a ten year old boy is put under the care of two fairy godparents, who can grant him almost any wish, which leads to dire consequences.")
add_show("The Good Wife", "Paramount+", ["Drama"], ["Dramatic", "Political"], "Serialized", "14", 156, 8.3, 81, "Alicia Florrick (Julianna Margulies) has been a good wife to her husband, a former state's attorney. After a very humiliating sex and corruption scandal, he is behind bars. She must now provide for her family and returns to work as a litigator in a law firm.")
add_show("Criminal Minds", "Paramount+", ["Crime", "Drama"], ["Dramatic", "Mysterious"], "Episodic", "14", 324, 8.1, 42, "The cases of the F.B.I. Behavioral Analysis Unit (B.A.U.), an elite group of profilers who analyze the nation's most dangerous serial killers and individual heinous crimes in an effort to anticipate their next moves before they strike again.")
add_show("NCIS", "Paramount+", ["Crime", "Drama"], ["Dramatic", "Mysterious"], "Episodic", "14", 425, 7.7, 51, "The cases of the Naval Criminal Investigative Service's Washington, D.C. Major Case Response Team, led by Special Agent Leroy Jethro Gibbs.")
add_show("Blue Bloods", "Paramount+", ["Drama", "Crime"], ["Dramatic", "Mysterious"], "Mixed", "14", 245, 7.6, 70, "Revolves around a family of New York cops.")
add_show("Spongebob Squarepants", "Paramount+", ["Comedy"], ["Witty", "Wacky", "Animated", "For Kids"], "Episodic", "Y7", 248, 8.2, 71, "The misadventures of a talking sea sponge who works at a fast food restaurant, attends a boating school, and lives in an underwater pineapple.")
add_show("Survivor", "Paramount+", ["Reality"], ["Competitive"], "Seasonal", "PG", 540, 7.3, 70, "A reality show where a group of contestants are stranded in a remote location with little more than the clothes on their back. The lone survivor of this contest takes home a million dollars.")

#Peacock Shows
add_show("House", "Peacock", ["Drama"], ["Witty", "Dry", "Dramatic"], "Episodic", "14", 177, 8.7, 75, "An antisocial maverick doctor who specializes in diagnostic medicine does whatever it takes to solve puzzling cases that come his way using his crack team of doctors and his wits.")
add_show("Law and Order: Special Victims Unit", "Peacock", ["Drama", "Crime"], ["Mysterious", "Provocative", "Witty"], "Episodic", "14", 505, 8.0, 66, "This series follows the Special Victims Unit, a specially trained squad of detectives in the N.Y.P.D., who investigate sexually related crimes.")
add_show("Parenthood", "Peacock", ["Drama", "Comedy"], ["Witty", "Dramatic", "Heartfelt"], "Serialized", "14", 103, 8.2, 64, "The lives and tragedies of the Braverman family tree.")
add_show("Downton Abbey", "Peacock", ["Drama", "Historical"], ["Dramatic", "Heartfelt"], "Serialized", "PG", 52, 8.7, 80, "A chronicle of the lives of the British aristocratic Crawley family and their servants in the early twentieth century.")
add_show("Friday Night Lights", "Peacock", ["Drama"], ["Dramatic", "Coming-of-Age"], "Serialized", "14", 76, 8.6, 83, "A drama that follows the lives of the Dillon Panthers, one of the nation's best high school football teams, and their head coach Eric Taylor.")
add_show("Yellowstone", "Peacock", ["Drama", "Western"], ["Gritty", "Dramatic", "Complex"], "Serialized", "MA", 39, 8.8, 54, "A ranching family in Montana faces off against others encroaching on their land.")
add_show("Vikings", "Peacock", ["Action", "Adventure", "Historical"], ["Epic", "Gritty", "Violent"], "Serialized", "MA", 89, 8.5, 74, "Vikings transports us to the brutal and mysterious world of Ragnar Lothbrok, a Viking warrior and farmer who yearns to explore - and raid - the distant shores across the ocean.")
add_show("Cheers", "Peacock", ["Comedy"], ["Witty", "Heartfelt"], "Mixed", "PG", 273, 7.9, 68, "The regulars of the Boston bar \"Cheers\" share their experiences and lives with each other while drinking or working at the bar where everybody knows your name.")
add_show("Parks and Recreation", "Peacock", ["Comedy"], ["Witty", "Wacky", "Heartfelt", "Easy-to-Watch"], "Mixed", "PG", 126, 8.6, 67, "The absurd antics of an Indiana town's public officials as they pursue sundry projects to make their city a better place.")
add_show("The Office", "Peacock", ["Comedy"], ["Witty", "Dry", "Irreverent"], "Mixed", "14", 201, 8.9, 66, "A mockumentary on a group of typical office workers, where the workday consists of ego clashes, inappropriate behavior, and tedium.")

#Disney+ Shows
add_show("The Beatles: Get Back", "Disney+", ["Documentary"], ["Nostalgic", "Emotional"], "Serialized", "14", 3, 9.1, 85, "Documentary about the music group The Beatles featuring in-studio footage that was shot in early 1969 for the 1970 feature film 'Let It Be.'")
add_show("What If?", "Disney+", ["Superhero"], ["Mind-Bending", "Violent", "Animated"], "Mixed", "14", 9, 7.5, 69, "Exploring pivotal moments from the Marvel Cinematic Universe and turning them on their head, leading the audience into uncharted territory.")
add_show("The Book of Boba Fett", "Disney+", ["Action", "Crime", "Science Fiction"], ["Gritty", "Nostalgic", "Epic"], "Serialized", "14", 6, 7.8, 59, "Bounty hunter Boba Fett & mercenary Fennec Shand navigate the underworld when they return to Tatooine to claim Jabba the Hutt's old turf.")
add_show("The Mandalorian", "Disney+", ["Adventure", "Action", "Western", "Science Fiction"], ["Epic", "Nostalgic", "Gritty", "Heartfelt"], "Mixed", "14", 16, 8.8, 71, "The travels of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.")
add_show("The Simpsons", "Disney+", ["Comedy"], ["Witty", "Irreverent", "Satirical", "Animated"], "Episodic", "14", 717, 8.6, 87, "The satiric adventures of a working-class family in the misfit city of Springfield.")
add_show("The Suite Life of Zack & Cody", "Disney+", ["Comedy"], ["Wacky", "For Kids"], "Episodic", "G", 87, 6.6, 54, "Comedy about identical twins living at the Tipton Hotel with their single mother who is a lounge singer at the hotel.")
add_show("Kim Possible", "Disney+", ["Comedy", "Action", "Crime"], ["Witty", "Coming-of-Age", "Animated", "For Kids"], "Mixed", "G", 87, 7.2, 63, "A high school cheerleader and her accident-prone best friend balance their duties as global crime-fighters with the typical challenges of adolescence.")
add_show("High School Musical: The Musical: The Series", "Disney+", ["Musical"], ["Dramatic", "Meta", "Witty", "Coming-of-Age"], "Serialized", "PG", 22, 7.1, 64, "The students from the school where the High School Musical films were shot stage a musical production based on the franchise.")
add_show("Loki", "Disney+", ["Superhero", "Adventure"], ["Witty", "Mind-Bending", "Complex", "Mysterious"], "Serialized", "14", 6, 8.3, 74, "The mercurial villain Loki resumes his role as the God of Mischief in a new series that takes place after the events of “Avengers: Endgame.”")
add_show("Wandavision", "Disney+", ["Superhero"], ["Meta", "Nostalgic", "Psychological", "Mind-Bending"], "Serialized", "14", 9, 8.0, 77, "Blends the style of classic sitcoms with the MCU, in which Wanda Maximoff and Vision - two super-powered beings living their ideal suburban lives - begin to suspect that everything is not as it seems.")

#HBO Max Shows
add_show("Lovecraft Country", "HBO Max", ["Horror", "Fantasy"], ["Dark", "Violent", "Provocative"], "Serialized", "MA", 10, 7.1, 79, "A young African-American travels across the U.S. in the 1950s in search of his missing father.")
add_show("I May Destroy You", "HBO Max", ["Drama"], ["Complex", "Provocative", "Dramatic"], "Serialized", "MA", 12, 8.1, 86, "The question of sexual consent in contemporary life and how, in the new landscape of dating and relationships, we make the distinction between liberation and exploitation.")
add_show("Band of Brothers", "HBO Max", ["Drama", "War", "Historical"], ["Gritty", "Violent", "Heartfelt", "Emotional"], "Serialized", "MA", 10, 9.4, 87, "The story of Easy Company of the U.S. Army 101st Airborne Division and their mission in World War II Europe, from Operation Overlord to V-J Day.")
add_show("ER", "HBO Max", ["Drama"], ["Dramatic"], "Mixed", "14", 331, 7.8, 79, "The lives, loves and losses of the doctors and nurses of Chicago's County General Hospital.")
add_show("Ed, Edd, n Eddy", "HBO Max", ["Comedy"], ["Irreverent", "Wacky", "Animated", "For Kids"], "Episodic", "Y7", 66, 7.4, 60, "The off-the-wall, day-to-day life of three friends who have exactly the same name.")
add_show("The West Wing", "HBO Max", ["Drama"], ["Witty", "Complex", "Political"], "Serialized", "14", 156, 8.8, 78, "Inside the lives of staffers in the West Wing of the White House.")
add_show("Barry", "HBO Max", ["Comedy", "Drama", "Crime"], ["Dark", "Witty", "Irreverent", "Violent", "Provocative"], "Serialized", "MA", 16, 8.3, 85, "A hit man from the Midwest moves to Los Angeles and gets caught up in the city's theatre arts scene.")
add_show("Watchmen", "HBO Max", ["Drama", "Action", "Superhero"], ["Dark", "Violent", "Gritty", "Complex", "Provocative", "Nostalgic"], "Serialized", "MA", 9, 8.2, 85, "Set in an alternate history where masked vigilantes are treated as outlaws, Watchmen embraces the nostalgia of the original groundbreaking graphic novel of the same name, while attempting to break new ground of its own.")
add_show("Chernobyl", "HBO Max", ["Drama", "Historical"], ["Dramatic", "Dark", "Provocative"], "Serialized", "MA", 5, 9.4, 82, "In April 1986, an explosion at the Chernobyl nuclear power plant in the Union of Soviet Socialist Republics becomes one of the world's worst man-made catastrophes.")
add_show("Veep", "HBO Max", ["Comedy"], ["Witty", "Satirical", "Political"], "Serialized", "MA", 65, 8.3, 82, "Former Senator Selina Meyer finds that being Vice President of the United States is nothing like she hoped and everything that everyone ever warned her about.")
add_show("Mare of Easttown", "HBO Max", ["Drama", "Crime"], ["Gritty", "Mysterious", "Dramatic"], "Serialized", "MA", 7, 8.5, 81, "A detective in a small Pennsylvania town investigates a local murder while trying to keep her life from falling apart.")
add_show("Succession", "HBO Max", ["Drama"], ["Witty", "Dramatic", "Provocative"], "Serialized", "MA", 20, 8.8, 83, "The Roy family is known for controlling the biggest media and entertainment company in the world. However, their world changes when their father steps down from the company.")
add_show("Euphoria", "HBO Max", ["Drama"], ["Provocative", "Dramatic", "Coming-of-Age"], "Serialized", "MA", 19, 8.4, 70, "A look at life for a group of high school students as they grapple with issues of drugs, sex, and violence.")
add_show("Westworld", "HBO Max", ["Drama", "Science Fiction"], ["Violent", "Dystopian", "Complex", "Mind-Bending", "Gritty"], "Serialized", "MA", 28, 8.6, 72, "Set at the intersection of the near future and the reimagined past, explore a world in which every human appetite can be indulged without consequence.")
add_show("The Sopranos", "HBO Max", ["Crime", "Drama"], ["Dark", "Witty", "Irreverent", "Gritty"], "Serialized", "MA", 86, 9.2, 94, "New Jersey mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect his mental state, leading him to seek professional psychiatric counseling.")
add_show("Game of Thrones", "HBO Max", ["Drama", "Fantasy"], ["Epic", "Violent", "Dark", "Gritty", "Provocative", "Complex", "Political"], "Serialized", "MA", 73, 9.2, 86, "Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.")
add_show("The Big Bang Theory", "HBO Max", ["Comedy"], ["Wacky", "Easy-to-Watch"], "Mixed", "14", 279, 8.1, 61, "A woman who moves into an apartment across the hall from two brilliant but socially awkward physicists shows them how little they know about life outside of the laboratory.")
add_show("Friends", "HBO Max", ["Comedy"], ["Witty", "Heartfelt", "Easy-to-Watch"], "Mixed", "14", 236, 8.8, 64, "Follows the personal and professional lives of six twenty to thirty-something-year-old friends living in Manhattan.")
add_show("Curb Your Enthusiasm", "HBO Max", ["Comedy"], ["Witty", "Irreverent", "Wacky", "Uncomfortable"], "Episodic", "MA", 100, 8.7, 84, "The life and times of Larry David and the predicaments he gets himself into with his friends and complete strangers.")
add_show("South Park", "HBO Max", ["Comedy"], ["Witty", "Irreverent", "Wacky", "Uncomfortable", "Animated"], "Mixed", "MA", 309, 8.7, 64, "Follows the misadventures of four irreverent grade-schoolers in the quiet, dysfunctional town of South Park, Colorado.")

#Hulu Shows
add_show("Atlanta", "Hulu", ["Comedy"], ["Witty", "Irreverent", "Provocative"], "Mixed", "MA", 21, 8.6, 93, "Based in Atlanta, Earn and his cousin Alfred try to make their way in the world through the rap scene. Along the way they come face to face with social and economic issues touching on race, relationships, poverty, status, and parenthood.")
add_show("The X-Files", "Hulu", ["Crime", "Drama", "Science Fiction"], ["Mysterious", "Mind-Bending"], "Mixed", "14", 218, 8.6, 65, "Two F.B.I. Agents, Fox Mulder the believer and Dana Scully the skeptic, investigate the strange and unexplained, while hidden forces work to impede their efforts.")
add_show("Love Island", "Hulu", ["Reality"], ["Competitive", "Dramatic", "Steamy", "Easy-to-Watch"], "Seasonal", "MA", 292, 5.2, 56, "Single hopefuls looking for love complete tasks, couple off and get voted out week by week. Packed full of drama.")
add_show("Malcolm in the Middle", "Hulu", ["Comedy"], ["Witty", "Irreverent", "Wacky", "Easy-to-Watch"], "Mixed", "PG", 151, 8.1, 88, "A gifted young teen tries to survive life with his dimwitted, dysfunctional family.")
add_show("Rick and Morty", "Hulu", ["Comedy"], ["Dark", "Witty", "Irreverent", "Provocative", "Cynical", "Animated"], "Mixed", "MA", 49, 9.2, 87, "An animated series that follows the exploits of a super scientist and his not-so-bright grandson.")
add_show("American Horror Story", "Hulu", ["Drama", "Horror"], ["Dark", "Provocative", "Mind-Bending"], "Seasonal", "MA", 103, 8.0, 65, "An anthology series centering on different characters and locations, including a house with a murderous past, an insane asylum, a witch coven, a freak show circus, a haunted hotel, a possessed farmhouse, a cult, the apocalypse, a slasher summer camp, and a bleak beach town and desert valley.")
add_show("The Handmaid's Tale", "Hulu", ["Drama", "Science Fiction"], ["Dystopian", "Mind-Bending", "Complex", "Dark"], "Serialized", "MA", 46, 8.4, 82, "Set in a dystopian future, a woman is forced to live as a concubine under a fundamentalist theocratic dictatorship.")
add_show("Adventure Time", "Hulu", ["Comedy"], ["Wacky", "Heartfelt", "Witty", "Animated", "For Kids"], "Mixed", "PG", 283, 8.6, 78, "A 12-year-old boy and his best friend, wise 28-year-old dog with magical powers, go on a series of surreal adventures with each other in a remote future.")
add_show("Fargo", "Hulu", ["Drama", "Crime", "Thriller"], ["Dark", "Mysterious"], "Serialized", "MA", 41, 8.9, 85, "Various chronicles of deception, intrigue and murder in and around frozen Minnesota. Yet all of these tales mysteriously lead back one way or another to Fargo, North Dakota.")
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
add_show("Cobra Kai", "Netflix", ["Comedy", "Drama", "Action"], ["Dramatic", "Irreverent", "Heartfelt", "Nostalgic", "Coming-of-Age"], "Serialized", "14", 40, 8.6, 70, "Decades after their 1984 All Valley Karate Tournament bout, a middle-aged Daniel LaRusso and Johnny Lawrence find themselves martial-arts rivals again.")
add_show("Breaking Bad", "Netflix", ["Drama", "Crime", "Thriller", "Western"], ["Dark", "Violent", "Gritty", "Complex"], "Serialized", "MA", 62, 9.4, 87, "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.")
add_show("Avatar: The Last Airbender", "Netflix", ["Adventure", "Fantasy"], ["Heartfelt", "Epic", "Animated", "Coming-of-Age", "For Kids"], "Serialized", "Y7", 54, 9.3, 84, "In a war-torn world of elemental magic, a young boy reawakens to undertake a dangerous mystic quest to fulfill his destiny as the Avatar, and bring peace to the world.")
add_show("Stranger Things", "Netflix", ["Adventure", "Science Fiction", "Horror"], ["Heartfelt", "Nostalgic", "Dark", "Coming-of-Age"], "Serialized", "14", 25, 8.7, 75, "When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces in order to get him back.")
add_show("The Last Dance", "Netflix", ["Documentary", "Biographical"], ["Nostalgic"], "Serialized", "MA", 10, 9.1, 90, "Charting the rise of the 1990's Chicago Bulls, led by Michael Jordan, one of the most notable dynasties in sports history.")
add_show("Making a Murderer", "Netflix", ["Documentary", "Crime"], ["Dark", "Provocative", "Dramatic"], "Serialized", "14", 20, 8.5, 77, "Filmed over a 10-year period, Steven Avery, a DNA exoneree who, while in the midst of exposing corruption in local law enforcement, finds himself the prime suspect in a grisly new crime.")
add_show("Too Hot to Handle", "Netflix", ["Reality"], ["Dramatic", "Steamy", "Provocative", "Competitive", "Easy-to-Watch"], "Serialized", "MA", 29, 4.6, 43, "On the shores of paradise, gorgeous singles meet and mingle. But there's a twist. To win a $100,000 grand prize, they'll have to give up sex.")
add_show("The Witcher", "Netflix", ["Fantasy", "Drama", "Action"], ["Dark", "Epic", "Violent", "Gritty"], "Serialized", "MA", 16, 8.2, 62, "Geralt of Rivia, a solitary monster hunter, struggles to find his place in a world where people often prove more wicked than beasts.")
add_show("Bojack Horseman", "Netflix", ["Comedy", "Drama"], ["Dark", "Dry", "Irreverent", "Animated", "Witty", "Provocative", "Complex"], "Serialized", "MA", 76, 8.7, 82, "BoJack Horseman was the star of the hit television show \"Horsin' Around\" in the '80s and '90s, but now he's washed up, living in Hollywood, complaining about everything, and wearing colorful sweaters.")
add_show("Love, Death & Robots", "Netflix", ["Science Fiction", "Thriller"], ["Dark", "Violent", "Animated", "Mind-Bending", "Dystopian", "Complex"], "Episodic", "MA", 26, 8.5, 65, "A collection of animated short stories that span various genres including science fiction, fantasy, horror and comedy.")
add_show("The Last Kingdom", "Netflix", ["Drama", "Historical", "Fantasy", "Action"], ["Dark", "Gritty", "Violent", "Epic"], "Serialized", "MA", 36, 8.4, 78, "As Alfred the Great defends his kingdom from Norse invaders, Uhtred--born a Saxon but raised by Vikings--seeks to claim his ancestral birthright.")
add_show("Squid Game", "Netflix", ["Drama", "Thriller"], ["Dark", "Gritty", "Political", "Dystopian", "Non-English"], "Serialized", "MA", 9, 8.0, 69, "Hundreds of cash-strapped players accept a strange invitation to compete in children's games. Inside, a tempting prize awaits with deadly high stakes. A survival game that has a whopping 45.6 billion-won prize at stake.")
add_show("Bodyguard", "Netflix", ["Drama", "Thriller", "Crime"], ["Gritty", "Dramatic", "Steamy"], "Serialized", "MA", 6, 8.1, 79, "A contemporary thriller featuring the Royalty and Specialist Protection Branch of London's Metropolitan Police Service.")
add_show("The Blacklist", "Netflix", ["Crime", "Thriller"], ["Mysterious", "Psychological"], "Mixed", "14", 174, 8.0, 74, "A new FBI profiler, Elizabeth Keen, has her entire life uprooted when a mysterious criminal, Raymond Reddington, who has eluded capture for decades, turns himself in and insists on speaking only to her.")
add_show("The Great British Baking Show", "Netflix", ["Reality"], ["Competitive", "Feel-Good", "Easy-to-Watch"], "Seasonal", "14", 50, 8.6, 82, "Bakers attempt three challenges each week trying to impress the judges enough to go through to the next round and eventually are crowned Britain's best amateur baker.")
add_show("Midnight Mass", "Netflix", ["Drama", "Horror"], ["Dark", "Psychological", "Provocative", "Mysterious", "Complex"], "Serialized", "MA", 7, 7.7, 75, "An isolated island community experiences miraculous events - and frightening omens - after the arrival of a charismatic, mysterious young priest.")
add_show("Schitt's Creek", "Netflix", ["Comedy"], ["Witty", "Irreverent", "Satirical", "Heartfelt", "Easy-to-Watch"], "Mixed", "MA", 80, 8.5, 73, "When rich video-store magnate Johnny Rose and his family suddenly find themselves broke, they are forced to leave their pampered lives to regroup in Schitt's Creek.")
add_show("Ozark", "Netflix", ["Crime", "Drama", "Thriller"], ["Dark", "Gritty", "Violent"], "Serialized", "MA", 37, 8.4, 69, "A financial advisor drags his family from Chicago to the Missouri Ozarks, where he must launder money to appease a drug boss.")
add_show("Dark", "Netflix", ["Horror", "Crime"], ["Mind-Bending", "Dark", "Psychological", "Mysterious"], "Serialized", "MA", 26, 8.8, 72, "A family saga with a supernatural twist, set in a German town, where the disappearance of two young children exposes the relationships among four families.")
add_show("Narcos", "Netflix", ["Crime", "Drama", "Thriller", "Historical"], ["Dark", "Gritty", "Violent"], "Serialized", "MA", 30, 8.8, 77, "A chronicled look at the criminal exploits of Colombian drug lord Pablo Escobar, as well as the many other drug kingpins who plagued the country through the years.")
add_show("The Queen's Gambit", "Netflix", ["Drama", "Historical"], ["Witty", "Dramatic", "Emotional"], "Serialized", "MA", 7, 8.6, 79, "Orphaned at the tender age of nine, prodigious introvert Beth Harmon discovers and masters the game of chess in 1960s USA. But child stardom comes at a price.")

#Helper function asks user about their streaming service availability and adds each service the user has to a list, then returns that list
def get_available_streaming_services():
    available_streaming_services = []
    for service in streaming_services:
        while True:
            available = scrollprint.scroll_input(f"\nDo you have {service}? y/n\n")
            if str(available).lower() == "y":
                scrollprint.scroll_print(f"\nGreat! We've added {service} shows to the available show list.\n")
                available_streaming_services.append(service)
                break
            elif str(available).lower() == "n":
                scrollprint.scroll_print("\nThat's too bad. Moving on...\n")
                break
            else:
                scrollprint.scroll_print("\nResponse not recognized. Please respond to prompts with 'y' or 'n'.\n")
    
    return available_streaming_services


#Helper function collects and returns information from user about preferred show genres/traits
def get_preferences(preference_lst, pref_cat):
    scrollprint.scroll_print(f"\nNow, let's collect some information about your favorite show {pref_cat}s. You must select at least one {pref_cat} to continue\n")
    help_str = f"\nTyping the beginning of a genre and pressing enter will generate a list of autocomplete suggestions\n\nTo add all {pref_cat}s to your preferences, type 'all'\n\nWhen you have specified all preferred {pref_cat}s, type 'done'\n\nType 'help' to bring up this guide again\n\n"
    preferences = []
    autocomp_preferences = []
    scrollprint.scroll_print(help_str)
    while True:
        preference = str(scrollprint.scroll_input(f"\nWhat {pref_cat} would you like to add to your preferences?\n")).lower()
        #User can only exit the function once they have added at least one item to their preference list
        if preference == "done":
            if len(preferences) == 0:
                scrollprint.scroll_print(f"\nYou must specify at least one {pref_cat} before finalizing\n")
            else:
                scrollprint.scroll_print(f"\nOkay, we have your {pref_cat} preferences\n")
                return preferences
        #User can specify all items as preferences
        elif preference == "all":
            scrollprint.scroll_print(f"\nOkay, clearly you don't have a {pref_cat} preference\n")
            preferences = preference_lst[:]
            return preferences
        #Brings up help message
        elif preference == "help":
            scrollprint.scroll_print(help_str)
        else:
            autocomp_preferences = []
            #Searches for matching substrings
            exact_match = False
            for item in preference_lst:
                if len(item) >= len(preference):
                    if item[0:len(preference)].lower() == preference:
                        if len(item) == len(preference):
                            exact_match = True
                            if item not in preferences:
                                #If scrollprint.scroll_input is exact match, adds preference to preferences list
                                scrollprint.scroll_print(f"\nAdding {item} to your preferences... done\n")
                                preferences.append(item)
                                break
                            else:
                                scrollprint.scroll_print(f"\n{item} is already in your preferences list! Please pick a different {pref_cat}\n")
                        #Adds autocomplete entry to list
                        else:
                            autocomp_preferences.append(item)
            if len(autocomp_preferences) > 0:
                print_str = "Autocomplete Suggestions: "
                for pref in autocomp_preferences:
                    print_str += f"{pref} | "
                print_str = print_str[:-3] + "\n"
                scrollprint.scroll_print(print_str)
            elif exact_match == True:
                pass
            else:
                scrollprint.scroll_print(f"\nNo matching {pref_cat}s found. Please try again.\n")


#Helper function asks user about their content rating limits and adds all content ratings at and below that limit to an allowed content rating list
def get_content_limit():
    while True:
        max_content_rating = scrollprint.scroll_input("\nWhat is the maximum content rating you want included in your recommendations? To view a list of content ratings, enter 'list'.\n")
        max_content_rating = str(max_content_rating).upper()
        #If max content rating matches, adds all content ratings at or below that max to the allowed content ratings list
        if max_content_rating in content_ratings.keys():
            for rating in content_ratings.keys():
                if rating == max_content_rating:
                    max_allowed_rating = content_ratings[rating]
                    scrollprint.scroll_print(f"\nYour maximum allowed content rating has been set to TV-{max_content_rating}\n")
                    return max_allowed_rating
        #Lists all content ratings if the user specifies
        elif max_content_rating == "LIST":
            msg = "\nContent Ratings: "
            for content_rating in content_ratings.keys():
                msg += content_rating + " | "
            #Trims off final 
            msg = msg[:-3] + "\n"
            scrollprint.scroll_print(msg)
        else:
            scrollprint.scroll_print("\nContent rating scrollprint.scroll_input was not recognized. Please enter a valid TV content rating. For a list of all content ratings, enter 'list'.\n")


#Helper function that collects from user whether they value critical reviews or user ratings when selecting a tv show
def user_or_critic():

    while True:
        preference = str(scrollprint.scroll_input("Do you value audience ratings ('audience') or critical reviews ('critics') more when deciding what shows to watch? Please enter your preference. If you don't have a preference, enter 'both'\n\n")).lower()

        if preference == "audience" or preference == "critics" or preference == "both":
            return preference
        else:
            scrollprint.scroll_print("\nInput not recognized. Please enter as a response either 'audience', 'critics', or 'both' to continue\n")


def run_recommender(show_dict):
    scrollprint.scroll_print("\nHello, and welcome to the streaming tv recommender tool!\n")
    scrollprint.scroll_print("\nTo start out, let's narrow down our choices to match the streaming services you have available.\n")
    shows_available = []
    available_streaming_services = get_available_streaming_services()

    #Adds shows from available streaming services to list of possible show recommendations
    for service in available_streaming_services:
        if service in available_streaming_services:
            shows_available += show_dict[service]
    
    #Has user select as many genres as they'd like for their search
    scrollprint.scroll_print("\nNow that we know what shows you can watch, let's narrow them down to which shows you want to watch.\n")
    genre_preferences = get_preferences(genres, "genre")
    
    #Has user select as many traits as they'd like for their search
    scrollprint.scroll_print("\nNext up, let's hear about what traits you like in a TV show.\n")
    trait_preferences = get_preferences(traits, "trait")
    
    #Collects user limitation on content rating
    scrollprint.scroll_print("Next up, we'll set your content rating filters.\n")
    max_content_rating = get_content_limit()

    #Collects user preference between user reviews and metacritic score
    scrollprint.scroll_print("\nFinally, we'll find out whether you value user ratings or critical reviews more when selecting a show.\n")
    review_preference = user_or_critic()

    #Loops through available tv shows and only keeps shows that match with user-specified preferences
    #Stores shows to recommend in max heap
    shows_to_recommend = maxheap.MaxHeap()
    for show in shows_available:
        genre_match = False
        trait_match = False
        #Checks genres, skips to next show if genres don't match
        for genre in show.genres:
            if genre in genre_preferences:
                genre_match = True
                break
        if genre_match == False:
            continue
        #Checks traits, skips to next show if traits don't match
        for trait in show.traits:
            if trait in trait_preferences:
                trait_match = True
                break
        if trait_match == False:
            continue
            #Checks content rating, adds show to recommendation heap if content rating falls in-bounds: if the show passes this test, it should be added to the recommendation list
        if content_ratings[show.content_rating] <= max_content_rating:
            #Assigns show a score dependent on whether the user indicated that they preferred critical reviews, audience scores, or both
            if review_preference == "critics":
                show.score = show.metacritic_rating
            elif review_preference == "audience":
                show.score = show.imdb_rating
            elif review_preference == "both":
                show.score = (show.metacritic_rating + show.imdb_rating*10)/2

            shows_to_recommend.add(show, show.score)

    #Takes top ten scoring shows from heap, or until heap is empty    
    top_ten_list = []
    for i in range(1, 11):
        if len(shows_to_recommend.items) <= 1:
            break
        top_ten_list.append(shows_to_recommend.pop()[0])
    #If top ten list is empty, then no shows were found matching user criteria
    if len(top_ten_list) == 0:
        scrollprint.scroll_print("\nSorry, we didn't find any shows matching your search criteria. Please feel free to try again\n")
    else:
        scrollprint.scroll_print("\n Generating your recommendations... see below!\n")
        for show in top_ten_list:
            scrollprint.scroll_print(str(show))

test_show = Series("Breaking Bad", "Netflix", ["Drama", "Crime", "Thriller", "Western"], ["Dark", "Violent", "Gritty", "Complex"], "Serialized", "MA", 62, 9.4, 87, "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.")

run_recommender(tv_shows)