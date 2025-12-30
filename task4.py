def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    a, b, c, d = map(int, input().split())
    num = a * d
    den = b * c
    g = gcd(num, den)
    print(num // g, den // g)


main()
