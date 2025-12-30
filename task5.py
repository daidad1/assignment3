 4def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    a, b, c, d = map(int, input().split())
    num = a*d - c*b
    den = b*d
    g = gcd(abs(num), den)
    print(num//g, den//g)


main()
