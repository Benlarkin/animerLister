class Anime:
    #this contains the attributes for a single anime show
    def __init__(self, title, episodes, genre, ranking):
        self.title = title
        self.episodes = episodes
        self.genre = genre
        self.ranking = ranking
    def get_Title(self):
        return self.title
    def get_Episodes(self):
        return self.episodes
    def get_Genre(self):
        return self.genre
    def get_Ranking(self):
        return self.ranking
    def set_Title(self, x):
        self.title = x
    def set_Episodes(self, x):
        self.episodes = x
    def set_Genre(self, x):
        self.genre = x
    def set_Ranking(self, x):
        self.ranking = x
    