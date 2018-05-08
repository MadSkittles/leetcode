def select_sort(l):
    for i in range(len(l) - 1):
        min_, min_pos = l[i], i
        for j in range(i + 1, len(l)):
            if l[j] < min_:
                min_, min_pos = l[j], j
        l[i], l[min_pos] = l[min_pos], l[i]


if __name__ == '__main__':
    l = [54, 2, 56, 12, 22, 46, 31, 67, 92, 52, 43, 54]
    select_sort(l)
    print(l)
