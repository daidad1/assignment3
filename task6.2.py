def main():
    a, b, c, d, diag = map(int, input().split())

    s1 = (a + b + diag) / 2
    s2 = (c + d + diag) / 2

    area = ((s1*(s1-a)*(s1-b)*(s1-diag))**0.5 +
            (s2*(s2-c)*(s2-d)*(s2-diag))**0.5)

    print(area)


main()
