class Knjiga:
    def __init__(self, naslov, autor, godina):
        self.naslov = naslov
        self.autor = autor
        self.godina = godina

        print(self.naslov)
        print(self.autor)
        print(self.godina)

knjiga1= Knjiga("Zločin i Kazna", "Fyodor Dostoevsky", "1866")
knjiga2= Knjiga("The Hobbit", "J.R.R. Tolkien", "1937")
