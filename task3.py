def hyp(a, b):
    return (a*a + b*b) ** 0.5


def main():
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    h1 = hyp(a1, b1)
    h2 = hyp(a2, b2)

    print(h1, h2)
    print("First bigger" if h1 > h2 else "Second bigger")


main()
