class BankovniRacun:
    def __init__(self, ime_vlasnika, broj_racuna, stanje):
        self.ime_vlasnika = ime_vlasnika
        self.broj_racuna = broj_racuna
        self.stanje = stanje

        self.stanje = 0.0

    def uplati(self, iznos):
        if iznos > 0:
            self.stanje = self.stanje + iznos
            print(f"Uplata na račun {self.stanje} je uspješno provedena.")
        else:
            print(f"Iznos uplate mora biti pozitivan.")
    
    def isplata(self, iznos):
        if iznos > 0:
            if iznos <= self.stanje:
                self.stanje = self.stanje + iznos
                print(f"Isplata na račun {self.stanje} je uspješno provedena.")
            else:
                print(f"Nemate dovoljno sredstava za uplatu.")
        else:
            print(f"Iznos uplate mora biti pozitivan.")       

    def info(self):
        print(f"Vlasnik računa {self.ime_vlasnika}")
        print(f"Broj racuna{self.broj_racuna}")
        print(f"Stanje{self.stanje}")