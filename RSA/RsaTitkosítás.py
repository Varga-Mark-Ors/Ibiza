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
    m = random.randint(10, 200)
    C = Gyorshatvanyozas2.gyorshatvany(m, e, N)
    m2 = KinaiMaradekTetel.kinai(C, d, P, Q)
    if m == m2 :
        print("A program megfelelően működik!")
    else:
        print("A program nem megfelelően működik!")
    #print("P =", P,", Q =", Q,", N =", N,", On =", On,", e =", e,", d =", d,)
    #print("C =", C, ", m = ", m, ", m2 = ", m2)
if __name__ == "__main__":
    main()