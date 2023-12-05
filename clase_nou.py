
# Clasa resurse

class Resurse:
    def __init__(self, hrana, lemn, piatra):
        self.hrana = hrana
        self.lemn = lemn
        self.piatra = piatra

# self din clasa respectiva, other din alta clasa

    def sum(self, other):
        return Resurse(self.hrana + other.hrana, self.lemn+other.lemn, self.piatra+other.piatra)

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
    nr_satean = 0
    def __init__(self, id_caracter):
        Caracter.__init__(self, id_caracter, viata=50, armura=0, atac=0)
        #Satean.ids.append(id_caracter)
        nr_satean +=1 
        self.cost = Resurse(50, 0, 0)

    def verifica_id(id_caracter: int) -> bool:
        if id_caracter in Satean.ids:
            return True
        return False


class Infanterist(Caracter):
    nr_infanetrist = 0
    def __init__(self, id_caracter):
        Caracter.__init__(self, id_caracter, viata=100, armura=1, atac=5)
        self.cost = Resurse(60, 80, 0)


class Cavaler(Caracter):
    nr_cavaler = 0
    def __init__(self, id_caracter):
        Caracter.__init__(self, id_caracter, viata=150, armura=2, atac=10)
        self.cost = Resurse(60, 80, 0)


class Erou(Caracter):
    erou_unic = 0    # verifica unicitatea 
    def __init__(self, id_caracter):
        Caracter.__init__(self, id_caracter, viata=150, armura=5, atact=15)
        self.cost = Resurse(0, 0, 0)


class Cladire:
    def __init__(self,scut, aur):
        self.scut = scut
        self.aur = aur



class Centru(Cladire):
    nr_centru = 0
    def __init__(self):
        Cladire.__init__(self, scut=50, aur=10)


class Cazarma(Cladire):
    def __init__(self):
        Cladire.__init__(self, scut=30, aur=20)
        self.cost=Resurse(0,50,100)
    nr_cazarma = 0


class Staul(Cladire):
    def __init__(self):
        Cladire.__init__(self, scut=20, aur=30)
        self.cost=Resurse(0,100,50)
    nr_staul = 0