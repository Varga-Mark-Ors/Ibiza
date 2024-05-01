from random import randint
from Euklidesz import euklidesz
from Gyorshatvanyozas2 import gyorshatvany
from KinaiMaradekTetel import kinai
from MillerRabin import MillerRabin

def kulcs():
    i = False
    while not i:
        Q = randint(3, 999)
        i = MillerRabin(Q) #Addig csináljuk míg prím számot nem kapunk
    #print(Q)
    i = False
    while not i:
        P = randint(3, 999)
        i = MillerRabin(P) #Addig csináljuk míg prím számot nem kapunk
    #print(P)
    N = P * Q
    On = (P - 1) * (Q - 1)
    i = False
    while not i:
        e = randint(3, On)
        dlista =list(euklidesz(On, e))
        if dlista[0] == 1: #Ha a On és e-nek az lnko-ja 1, akkor jók a számok és mehetünk tovább velük
            i = True
            d = dlista[2] # d értéke az y lesz
    return P, Q, N , On, e, d 


def main():
    (P, Q, N , On, e, d) = list( kulcs() )
    m = randint(10, 200)
    S = kinai(m, d, P, Q) #Titkosítjuk az aláírást
    S2 = gyorshatvany(S, e, N) #Kikódoljuk azt
    if m == S2 : #Ha ugyan azt kapjuk megfelelően megy a program
        print("A program megfelelően működik!")
    else:
        print("A program nem megfelelően működik!")
if __name__ == "__main__":
    main()