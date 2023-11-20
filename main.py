from clase import Resurse, Caracter, Satean, Cavaler, Infanterist, Centru, Cazarma, Staul, Cladire
from game import Joc


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
    cv1 = joc_vikingi.creeaza_cavaler(1)
    print(type(cv1))