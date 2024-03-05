
def sorm(a, s):
    #print(a)
    if (a == 1):
        s = s + "1"
        return s
    else:
        if (a % 2 == 0):
            s = s + "0"
            return sorm(a // 2, s)
        else:
            s = s + "1"
            return sorm(a // 2, s)


def gyorshatvany(alap, exp, mod):
    sor =""
    sor = sorm(exp, sor)
    sor = [i for i in sor]
    e = 1
    alap2 = alap
    #print(len(sor))
    for i in range(len(sor)):
        #print(alap2)
        if sor[i] == "1":
            e *= alap2 
            e %= mod
        alap2 = (alap2 ** 2 % mod)
        #if sor[i] == "1":
        #    e *= (alap ** (2 ** i) % mod) 

    return e 
    
def main():
    print(gyorshatvany(69, 420, 123))
    print(gyorshatvany(129, 97, 171))
    print(gyorshatvany(6, 73, 100))
if __name__ == "__main__":
    main()