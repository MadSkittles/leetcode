class Solution(object):
    def getSkyline(self, buildings):
        import bisect
        buildings.sort(key=lambda x: x[2])
        axis, heights = [float('-inf'), float('inf')], [0, 0]

        for l, r, h in buildings:
            idl = bisect.bisect_left(axis, l)
            idr = bisect.bisect_right(axis, r)

            if h == heights[idl - 1]:
                axis[idl: idr] = [r]
                heights[idl: idr] = [heights[idr - 1]]
            else:
                axis[idl: idr] = [l, r]
                heights[idl: idr] = [h, heights[idr - 1]]

        return [[axis[i], heights[i]] for i in range(1, len(axis) - 1)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.getSkyline([[3, 7, 15],[5, 12, 12]]))
