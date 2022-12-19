class artist():
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
        return f'Performer: {self.artist}\nSong {self.title}\nAlbum: {self.album}\nYear: {self.year}'


s1 = artist("Maryla Rodowicz", "W sumie nie jest źle", "Ach Świecie", 2017)
print(s1)
s2 = artist("Taco Hemingway", "Marsz, Marsz", "Trójkąt Warszawski", 2014)
print(s2)