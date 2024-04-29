def sorm(a, s):
    #print(a)
    if (a == 1): #Addig megyünk míg a szám nem osztható tovább 2-vel
        s = s + "1"
        return s
    else:
        if (a % 2 == 0):
            s = s + "0" #Ha osztható 2-vel 0-t rakunk bele a stringbe, ha nem akkor 1-t
            return sorm(a // 2, s)
        else:
            s = s + "1"
            return sorm(a // 2, s)


def gyorshatvany(alap, exp, mod):
    sor ="" #Csinálunk egy üres stringet
    sor = sorm(exp, sor) #Az exp átalakítjuk 2-s számrendszerbe
    sor = [i for i in sor] #Listává alakítjuk át
    e = 1
    alap2 = alap
    for i in range(len(sor)): #végig megyünk a listán
        if sor[i] == "1":
            e *= alap2 #Ahol 1-s volt ott behelyetesítünk a képletbe
            e %= mod
        alap2 = (alap2 ** 2 % mod) #alap2-t meg tovább számoljuk

    return e #vissza adjuk az eredményt
    
def main():
    print(gyorshatvany(69, 420, 123))
    print(gyorshatvany(129, 97, 171))
    print(gyorshatvany(6, 73, 100))
if __name__ == "__main__":
    main()