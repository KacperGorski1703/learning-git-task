class movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0
    def play(self, step=1):
        self.views += step
    def __str__(self):
        return f'{self.title} ({self.year})'

class series(movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    def __str__(self):
        return f'{self.title} {self.year} (S{self.season}E{self.episode})'

movie_1 = movie(title="AntMan", year=2015, genre="Action")
movie_2 = movie(title="Thor Love and Thunder", year=2022, genre="Action")
movie_3 = movie(title="Top Gun Maverick", year=2022, genre="Action")
movie_4 = movie(title="Greenbook", year=2018, genre="Drama")

series_1 = series(episode="01", season="01", title="test", year=1999, genre="testing")
series_2 = series(episode="01", season="01", title="Stranger Things", year=2016, genre="Horror")
series = [series_1,series_2]


print(movie)