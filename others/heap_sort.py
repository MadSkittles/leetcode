def adjust_top(l, start=0, end=None):
    cur, end = start, len(l) - 1 if end is None else end
    while 2 * cur + 1 <= end:
        child = 2 * cur + 1 + (2 * cur + 2 <= end and l[2 * cur + 2] > l[2 * cur + 1])
        if l[child] > l[cur]:
            l[cur], l[child] = l[child], l[cur]
            cur = child
        else:
            break


def heapify(l):
    for i in range(len(l) // 2)[::-1]:
        adjust_top(l, start=i)


def heap_sort(l):
    heapify(l)
    for i in range(1, len(l))[::-1]:
        l[0], l[i] = l[i], l[0]
        adjust_top(l, end=i - 1)


if __name__ == "__main__":
    l = [54, 2, 56, 12, 22, 46, 31, 67, 92, 52, 43, 54]
    heap_sort(l)
    print(l)
