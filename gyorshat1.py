
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
    
def main():
    print(gyorshatvany(69, 420, 123))
    print(gyorshatvany(129, 97, 171))
    print(gyorshatvany(6, 73, 100))
if __name__ == "__main__":
    main()