import math


def get_arc(p, p0):
    res = math.atan2(p[1] - p0[1], p[0] - p0[0])
    return res + (2 * math.pi if res < 0 else 0)


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def graham_scan(points):
    k = 0
    for i in range(1, len(points)):
        if (points[i][1], points[i][0]) < (points[k][1], points[k][0]):
            k = i
    points[0], points[k] = points[k], points[0]
    points[1:] = sorted(points[1:], key=lambda x: (get_arc(x, points[0]), distance(x, points[0])))
    stack = points[:3]
    for p in points[3:]:
        while len(stack) > 1 and get_arc(p, stack[-2]) <= get_arc(stack[-1], stack[-2]):
            stack.pop()
        stack.append(p)
    return stack


if __name__ == '__main__':
    points = [(9, 100), (200, 400), (300, 400), (400, 300), (400, 400), (500, 400), (500, 200), (350, 200), (200, 200)]
    print(graham_scan(points))
