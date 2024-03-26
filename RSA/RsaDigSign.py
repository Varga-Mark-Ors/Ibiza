import random
import Euklidesz
import Gyorshatvanyozas2
import KinaiMaradekTetel

def prim(a):
    for j in range(2, a // 2):
        if a % j == 0:
            return False
    return True

def kulcs():
    i = False
    while not i:
        Q = random.randint(3, 999)
        i = prim(Q)
    #print(Q)
    i = False
    while not i:
        P = random.randint(3, 999)
        i = prim(P)
    #print(P)
    N = P * Q
    On = (P - 1) * (Q - 1)
    i = False
    while not i:
        e = random.randint(3, On)
        dlista =list(Euklidesz.euklidesz(On, e))
        if dlista[0] == 1:
            i = True
            d = dlista[2]
    return P, Q, N , On, e, d 


def main():
    (P, Q, N , On, e, d) = list(kulcs())
    #print(P, Q, N , On, e, d)
    m = random.randint(10, 200)
    S = KinaiMaradekTetel.kinai(m, d, P, Q)
    #print(S)
    S2 = Gyorshatvanyozas2.gyorshatvany(S, e, N)
    if m == S2 :
        print("A program megfelelően működik!")
    else:
        print("A program nem megfelelően működik!")
if __name__ == "__main__":
    main()