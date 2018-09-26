def head_adjust(l, s, end=None):
    end = len(l) if end is None else end
    child = 2 * s + 1
    while child < end:
        if child < end - 1 and l[child] < l[child + 1]:
            child += 1
        if l[s] < l[child]:
            l[s], l[child] = l[child], l[s]
            s, child = child, 2 * child + 1
        else:
            break


def heapify(l):
    for i in range(len(l) // 2 - 1, -1, -1):
        head_adjust(l, i)


def heap_sort(l):
    heapify(l)
    for i in range(len(l) - 1, 0, -1):
        l[0], l[i] = l[i], l[0]
        head_adjust(l, 0, i)


if __name__ == '__main__':
    l = [54, 2, 56, 12, 22, 46, 31, 67, 92, 52, 43, 54]
    heap_sort(l)
    print(l)
