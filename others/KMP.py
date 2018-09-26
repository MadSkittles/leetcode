def get_lps(needle):
    lps = [0]
    for i in range(1, len(needle)):
        index = lps[i - 1]
        while index > 0 and needle[index] != needle[i]:
            index = lps[index - 1]
        lps.append(index + (needle[index] == needle[i]))
    return lps


def kmp(haystack, needle):
    if len(needle) > len(haystack):
        return -1
    if not needle:
        return 0

    lps = get_lps(needle)

    j = 0
    for i in range(len(haystack)):
        while j > 0 and needle[j] != haystack[i]:
            j = lps[j - 1]
        if needle[j] == haystack[i]:
            j += 1
        if j == len(needle):
            return i - len(needle) + 1
    return -1


if __name__ == "__main__":
    print(kmp("aaaacecaaaaaacecaaabaaacaabaaabaaac", "aacecaaaaaacecaa"))
