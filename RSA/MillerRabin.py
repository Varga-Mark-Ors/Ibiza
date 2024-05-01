
def Prime(a, b):
    return a == b

def MillerRabin(n : int) -> bool:
    i = False
    d = n
    n -= 1
    S = 0
    while not i:
        n = n // 2
        S += 1
        if n % 2 == 1:
            i = True
    d, n = n, d
    S1 = S
    alap = (2 ** (d ** (2 ** (S1 - S)))) % n
    if Prime(alap, n - 1):
        return True
    S -= 1
    while S > 0:
        S -= 1
        alap = (alap ** 2) % n
        if Prime(alap, n - 1):
            return True

    return False

def main():
    print(MillerRabin(257))
    print(MillerRabin(683))
    print(MillerRabin(397))
    print(MillerRabin(561))
    print(MillerRabin(399))
    print(MillerRabin(525))
if __name__ == '__main__':
    main()