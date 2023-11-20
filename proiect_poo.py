# Clasa resurse

class Resurse:
    def __init__(self, hrana, lemn, piatra):
        self.hrana = hrana
        self.lemn = lemn
        self.piatra = piatra

# self din clasa respectiva, other din alta clasa

    def sum(self, other):
        return Resurse(self.hrana + other.hrana, self.lemn+other.lemn, self.piatra+other.lemn)

    def dif(self, other):
        return Resurse(max(0, (self.hrana-other.hrana)), max(0, self.lemn-other.lemn), max(0, self.piatra-other.piatra))

    def afis(self):
        return f"Hrana: {self.hrana}, Lemn: {self.lemn}, Piatra: {self.piatra}"

    def verif(self, other):
        return self.hrana >= other.hrana and self.lemn >= other.lemn and self.piatra >= other.piatra


# Clasa caractere
class Caracter:
    def __init__(self, id_caracter, viata, armura, atac):
        self.id_caracter = id_caracter
        self.viata = viata
        self.armura = armura
        self.atac = atac


class Satean(Caracter):
    ids = []

    def __init__(self, id_caracter):
        Caracter.__init__(self, id_caracter, viata=50, armura=0, atac=0)
        Satean.ids.append(id_caracter)
        self.cost = Resurse(50, 0, 0)

    def verifica_id(id_caracter: int) -> bool:
        if id_caracter in Satean.ids:
            return True
        return False


class Infanterist(Caracter):
    def __init__(self, id_caracter):
        Caracter.__init__(self, id_caracter, viata=100, armura=1, atac=5)
        self.cost = Resurse(60, 80, 0)


class Cavaler(Caracter):
    def __init__(self, id_caracter):
        Caracter.__init__(self, id_caracter, viata=150, armura=2, atac=10)
        self.cost = Resurse(60, 80, 0)


class Erou(Caracter):
    def __init__(self, id_caracter):
        Caracter.__init__(self, id_caracter, viata=150, armura=5, atact=15)
        self.cost = Resurse(0, 0, 0)


class Cladire:
    def __init__(self, scut, aur):
        self.scut = scut
        self.aur = aur



class Centru(Cladire):
    def __init__(self):
        Cladire.__init__(self, scut=50, aur=10)


class Cazarma(Cladire):
    def __init__(self):
        Cladire.__init__(self, scut=30, aur=20)
        self.cost=Resurse(0,50,100)



class Staul(Cladire):
    def __init__(self):
        Cladire.__init__(self, scut=20, aur=30)
        self.cost=Resurse(0,100,50)


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
            return "Ati creat cazarma"
        else:
            return "Nu aveti resurse necesare"
        
    def creeaza_staul(self):
        staul=Staul()
        if self.resurse_initiale.verif(staul.cost):
            self.resurse_initiale = self.resurse_initiale.dif(staul.cost)
            return "Ati creat staul"
        else:
            return "Nu aveti resurse necesare"




if __name__ == "__main__":

    r_vik = Resurse(100, 150, 150)
    print(r_vik.afis())

    joc_vikingi = Joc(r_vik, "Vikingi")

    s1 = joc_vikingi.creeaza_satean(1)
    s2 = joc_vikingi.creeaza_satean(2)

    print(s1.cost.afis())
    print(s1.id_caracter)
    print(s2.id_caracter)

    print(joc_vikingi.resurse_initiale.afis())

    joc_vikingi.munceste(3, "hrana")
    print("\n")
    print(joc_vikingi.resurse_initiale.afis())
    #joc_vikingi.resurse_initiale=Resurse(0,0,0)
    print(joc_vikingi.creeaza_cazarma())
    print(joc_vikingi.resurse_initiale.afis())
    print("\n\n")
    print(joc_vikingi.creeaza_staul())
    print(joc_vikingi.resurse_initiale.afis())

