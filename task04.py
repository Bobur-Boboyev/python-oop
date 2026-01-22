class Movie:

    def __init__(self, title: str, genre: str, duration: int | float, rating: int | float):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

m01 = Movie("Sehrli Qalpoqcha", "Comedy", 1.23, 9.0)

print(m01.title)
print(m01.genre)
print(m01.duration)
print(m01.rating)

