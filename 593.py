class Solution:
    def validSquare(self, p1, p2, p3, p4):
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        dis = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        return dis(p1, p2) == dis(p3, p4) == dis(p1, p3) == dis(p2, p4) > 0 and dis(p1, p4) == dis(p2, p3)