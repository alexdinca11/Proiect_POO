from clase import Resurse, Caracter, Satean, Cavaler, Infanterist, Centru, Cazarma, Staul, Cladire

class Joc:
    def __init__(self, resurse_initiale, civilizatie):
        self.resurse_initiale = resurse_initiale
        self.civilizatie = civilizatie

    def creeaza_satean(self, id_satean):
        satean = Satean(id_satean)
        if self.resurse_initiale.verif(satean.cost):
            self.resurse_initiale = self.resurse_initiale.dif(satean.cost)
            return satean
        else:
            return None

    def munceste(self, id_satean, tip_resursa):
        if Satean.verifica_id(id_satean) == False:
            print(f'Caracterul cu id-ul {id_satean} nu exista!\n')
        else:
            self.tip_resursa = tip_resursa

            if self.tip_resursa == "hrana":
                self.resurse_initiale = self.resurse_initiale.sum(
                    Resurse(50, 0, 0))
            elif self.tip_resursa == "lemn":
                self.resurse_initiale = self.resurse_initiale.sum(
                    Resurse(0, 50, 0))
            elif self.tip_resursa == "piatra":
                self.resurse_initiale = self.resurse_initiale.sum(
                    Resurse(0, 0, 50))
                

    def creeaza_cazarma(self):
        cazarma=Cazarma()
        if self.resurse_initiale.verif(cazarma.cost):
            self.resurse_initiale = self.resurse_initiale.dif(cazarma.cost)
            Cazarma.nr_cazarma += 1
            return "Ati creat cazarma"
        else:
            return "Nu aveti resurse necesare"
    
    def creeaza_infanterist(self, id_infanterist):
        infanterist = Infanterist(id_infanterist)
        if self.resurse_initiale.verif(infanterist.cost) and Cazarma.nr_cazarma:
            self.resurse_initiale = self.resurse_initiale.dif(infanterist.cost)
            return infanterist
        else:
            return None

    def creeaza_staul(self):
        staul=Staul()
        if self.resurse_initiale.verif(staul.cost):
            self.resurse_initiale = self.resurse_initiale.dif(staul.cost)
            Staul.nr_staul += 1
            return "Ati creat staul"
        else:
            return "Nu aveti resurse necesare"

    def creeaza_cavaler(self, id_cavaler):
        cavaler = Cavaler(id_cavaler)
        if self.resurse_initiale.verif(cavaler.cost):
            self.resurse_initiale = self.resurse_initiale.dif(cavaler.cost)
            print("proba")
            return cavaler
        else:
            print("proba2")
            return None
