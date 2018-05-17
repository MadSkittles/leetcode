def multiply(p1, p2, p0):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def graham_scan(points):
    from functools import cmp_to_key
    k = 0
    for i in range(1, len(points)):
        if (points[i][1], points[i][0]) < (points[k][1], points[k][0]):
            k = i
    points[0], points[k] = points[k], points[0]
    points[1:] = sorted(points[1:], key=cmp_to_key(lambda x, y: -multiply(x, y, points[0]) or (distance(x, points[0] - distance(y, points[0])))))
    print(points)
    stack = points[:3]
    for p in points[3:]:
        while len(stack) > 1 and multiply(p, stack[-1], stack[-2]) >= 0:
            stack.pop()
        stack.append(p)
    return stack


if __name__ == '__main__':
    points = [(9, 100), (200, 400), (300, 400), (400, 300), (400, 400), (500, 400), (500, 200), (350, 200), (200, 200)]
    print(graham_scan(points))
