def euklidesz(k0, k1, d = 0, x = 0, y = 0):
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
    return d, x, y #vissza adjuk az értékeket

def main():
    print(euklidesz(2756, 182))
    print(euklidesz(544, 119))
    print(euklidesz(280, 3))
    
   # a = int(input("Első szám:"))
   # b = int(input("Második szám:"))
   # print(Euklidesz(a, b))

if __name__=="__main__":
    main()