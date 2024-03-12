def gyorshatvany(alap, exp, mod):
    alap = alap % mod
    if (exp == 0):
        return 0
    elif (exp == 1):
        return alap
    elif (exp // 2 ==0):
        return gyorshatvany(alap * alap % mod, exp/2, mod)
    else:
        return alap * gyorshatvany(alap, exp - 1, mod) % mod
    
def gyorshatvany2(alap, exp, mod, s):
    if s != 0 :
        s -= 1
        alap = alap % mod
        if (exp == 0):
            return 0
        elif (exp == 1):
            return alap
        elif (exp // 2 ==0):
            return gyorshatvany(alap * alap % mod, exp/2, mod)
        else:
            return alap * gyorshatvany(alap, exp - 1, mod) % mod
    else:
        return alap * gyorshatvany(alap, exp - 1, mod) % mod
    
def Smeghat(n):
    s = 1
    while (n // 2) % 2 == 0:
        n = n // 2
        s += 1
    return s 

def ferm(n):
    s = Smeghat(n)
    #print(s)
    d = n // (2**s)
    #print(d)
    meg1 = (gyorshatvany(2, d, n))
    if meg1 == 1 :
        return "Prím - 1 lépésre"
    else:
        meg2 = gyorshatvany2(2, d, n, s - 1)
        #print(meg2)
        if meg2 == (n - 1):
            return "Prím - 2 lépésre"
        else:
            return "Nem prím!"
        
        ##### második részen lehet specifikus fg írni, hogy efficiensebb legyen

def main():
    print(ferm(491))
    print(ferm(561))
    print(ferm(571))
    print(ferm(771))
    print(ferm(991))
if __name__ == "__main__":
    main()