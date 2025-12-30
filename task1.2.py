def main():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))

    for arr in [arr1, arr2, arr3]:
        s = sum(arr)
        avg = s / len(arr)
        print(s, avg)


main()
