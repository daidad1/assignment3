def inside(x, y, r, px, py):
    return (px-x)**2 + (py-y)**2 <= r*r


def main():
    x, y, r = map(int, input().split())
    points = [(1,2), (3,4), (0,0)]

    count = 0
    for p in points:
        if inside(x, y, r, p[0], p[1]):
            count += 1

    print(count)


main()
