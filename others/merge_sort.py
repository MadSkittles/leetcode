def merge_sort(l, start=0, end=None):
    end = len(l) - 1 if end is None else end
    if start < end:
        mid = (start + end) // 2
        merge_sort(l, start, mid)
        merge_sort(l, mid + 1, end)

        tmp, i, j = [], start, mid + 1
        while i <= mid or j <= end:
            if i <= mid and ((j <= end and l[i] <= l[j]) or j > end):
                tmp.append(l[i])
                i += 1
            elif j <= end and ((i <= end and l[j] < l[i]) or i > mid):
                tmp.append(l[j])
                j += 1
        l[start:end + 1] = tmp[:]


if __name__ == '__main__':
    l = [54, 2, 56, 12, 22, 46, 31, 67, 92, 52, 43, 54]
    merge_sort(l)
    print(l)
