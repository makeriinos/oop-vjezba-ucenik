
class Ucenik:
    """
    Nacrt (klasa) za stvaranje objekata koji predstavljaju učenike.
    Svaki učenik ima ime, prezime, razred i listu ocjena.
    """

    # Konstruktor - posebna metoda koja se poziva pri stvaranju novog objekta
    def __init__(self, ime, prezime, razred):
        """Inicijalizira novi objekt Učenik s početnim podacima."""
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = []  # Atribut 'ocjene' se inicijalizira kao prazna lista

    # Metode - funkcije unutar klase koje definiraju što objekt može raditi
    def dodaj_ocjenu(self, ocjena):
        """Dodaje novu ocjenu u listu ocjena učenika."""
        if isinstance(ocjena, int) and 1 <= ocjena <= 5:
            self.ocjene.append(ocjena)
            print(f"INFO: Učeniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.")
        else:
            print(f"GREŠKA: Ocjena '{ocjena}' nije važeća. Molimo unesite broj od 1 do 5.")

    def izracunaj_prosjek(self):
        """Vraća prosjek svih ocjena učenika."""
        # Provjera ako je lista ocjena prazna da se izbjegne dijeljenje s nulom
        if not self.ocjene:
            return 0.0
        
        return sum(self.ocjene) / len(self.ocjene)

    def info(self):
        """Ispisuje sve dostupne informacije o učeniku na konzolu."""
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        
        # Ispis ocjena, ili poruka ako nema ocjena
        if self.ocjene:
            print(f"Ocjene: {self.ocjene}")
        else:
            print("Ocjene: (nema upisanih ocjena)")
            
        prosjek = self.izracunaj_prosjek()
        print(f"Prosjek ocjena: {prosjek:.2f}") # Formatiranje na dvije decimale
        print("-" * 30)




#glavni dio



def ispisi_izbornik():
    print('-' +'='*20 + '-')
    print('Glavni izbornik')
    print('-' +'='*20 + '-')
    print('0- Izlaz iz programa')
    print('1- Unos novog učenika')
    print('2- Unos ocjene učeniku')
    print('3- Ispis podataka o učeniku')

def upisUcenika(ime, prezime, razred):
    ucenik = Ucenik(ime, prezime, razred)
    return ucenik

def upisOcjene(ucenik, ocjena):
    ucenik.dodaj_ocjenu(ocjena)

def ispisUcenika(ucenik):
    ucenik.info()
    
lista_ucenika = []
while True:
    ispisi_izbornik()
    try:  
        odgovor = int(input('Odaberite opciju (0/1/2/3): '))
        if odgovor == 0:
            print("Izlaz iz programa. Doviđenja!")
            break
        elif odgovor == 1:
            print('Unos novog učenika:')
            ime = input("Unesite ime učenika: ")
            prezime = input("Unesite prezime učenika: ")
            razred = input("Unesite razred učenika: ")
            ucenik = upisUcenika(ime, prezime, razred)
            lista_ucenika.append(ucenik)
            print(f"INFO: Učenik {ime} {prezime} uspješno unesen.")
        elif odgovor == 2:
            print('Unos ocjene učeniku:')
            ime = input("Unesite ime učenika: ")
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:                                  
                    ocjena = int(input("Unesite ocjenu (1-5): "))
                    upisOcjene(ucenik, ocjena)
                else:
                    print(f"GREŠKA: Učenik s imenom '{ime}' nije pronađen.")
            
        elif odgovor == 3:
            print('Ispis podataka o učeniku:')
            ime = input("Unesite ime učenika: ")
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:                                  
                    ispisUcenika(ucenik)
                else:
                    print(f"GREŠKA: Učenik s imenom '{ime}' nije pronađen.")
            
        
    except ValueError:
        print("GREŠKA: Molimo unesite brojčanu vrijednost.")
        continue


for ucenik in lista_ucenika:
        ucenik.info()

        
    



        


