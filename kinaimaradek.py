def Euklidesz(k0, k1, d = 0, x = 0, y = 0):
    x0 = 1 #Tábláyat első 2 sora xk,yk-nak
    x1 = 0
    y0 = 0
    y1 = 1
    s = 1
    while (k1 != 0): #amíg nem kapunk 0-t megy tovább
        maradek = k0 % k1
        qk = k0 // k1 
        k0 = k1  
        k1 = maradek  # ha k1 = 0 megfog állni és a k1 lesz az lnko
        x = x1
        y = y1 #lementjük a x1,y1-t
        x1 = (qk * x1) + x0
        y1 = (qk * y1) + y0 #kiszámoljuk az új xk,yk-t
        x0 = x
        y0 = y #vissza adjuk a lementett x1,y1 (volt) értékeket
        s *= -1 # növeljűk a k-t úgymond, hogy k + 1-t változtatjuk
    x = s * x0 # képletbe behelyetesítve megkapjuk az x-t
    y = -s * y0 # képletbe behelyetesítve megkapjuk az y-t
    d = k0 # oda adjuk a d-nek az lnko-t
    #print(x,y)
    return x, y #vissza adjuk az értékeket

def kinai(C, d, P, Q):
    m1 = Q # Képlet pontosabban (P*Q) / P
    m2 = P # Képlet pontosabban (P*Q) / Q
    c1 = C ** (d % (m2 - 1)) % m2
    #print(c1)
    c2 = C ** (d % (m1 - 1)) % m1
    #print(c2)
    (y1, y2) = Euklidesz(m1, m2)
    #print(y1," ",y2)
    m = y1 * m1 * c1 + m2 * y2 * c2
    m = m % (P * Q)
    print("m =", m)


def main():
    kinai(15,23,5,11)
if __name__ == "__main__":
    main()