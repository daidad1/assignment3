def triangle_area(a, h):
    return a * h / 2


def main():
    a = float(input())
    h = a * 0.866
    area = 6 * triangle_area(a, h)
    print(area)


main()
