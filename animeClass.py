class Anime:
    #this contains the attributes for a single anime show
    def __init__(self, title, episodes, genre, ranking):
        self.title = title
        self.episodes = episodes
        self.genre = genre
        self.ranking = ranking
    def getTitle(self):
        return self.title
    def getEpisodes(self):
        return self.episodes
    def getGenre(self):
        return self.genre
    def getRanking(self):
        return self.ranking