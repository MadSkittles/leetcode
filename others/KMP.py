def kmp(haystack, needle):
    if len(needle) > len(haystack):
        return -1
    if not needle:
        return 0
    next_group, point, i = [0] * len(needle), -1, 0
    next_group[0] = -1
    while i < len(needle) - 1:
        if point == -1 or needle[i] == needle[point]:
            point += 1
            i += 1
            next_group[i] = point
        else:
            point = next_group[point]

    i = j = 0
    while i < len(haystack) and j < len(needle):
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = next_group[j]
    if j == len(needle):
        return i - j
    else:
        return -1


if __name__ == "__main__":
    print(kmp("aabaaabaaac", "aabaaac"))
