l = [5, -3, 5, 5, -3, 5]
size = 3
n = s = l[-1]
pos = len(l) - 1
for i in range(len(l) - 2, len(l) - 1 - 3, -1):
    n += l[i]
    if n >= s:
        s = n
        pos = i
diff = sum(l[len(l) - 3 : pos])
for i in range(len(l) - 1, -1, -1):
    pass
