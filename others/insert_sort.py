def insert_sort(l):
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            x, j = l[i], i - 1
            while j >= 0 and x < l[j]:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = x


if __name__ == '__main__':
    l = [54, 2, 56, 12, 22, 46, 31, 67, 92, 52, 43, 54]
    insert_sort(l)
    print(l)
