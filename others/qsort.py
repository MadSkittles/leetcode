def qsort(l, start, end):
    if start > end:
        return
    lo, hi, pivot = start, end, l[start]
    while lo < hi:
        while l[hi] >= pivot and lo < hi:
            hi -= 1
        while l[lo] <= pivot and lo < hi:
            lo += 1
        if lo < hi:
            l[lo], l[hi] = l[hi], l[lo]
    l[start], l[lo] = l[lo], pivot
    qsort(l, start, lo - 1)
    qsort(l, lo + 1, end)


if __name__ == "__main__":
    l = [54, 2, 56, 12, 22, 46, 31, 67, 92, 52, 43, 54]
    qsort(l, 0, len(l) - 1)
    print(l)
