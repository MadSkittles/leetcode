class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        self.graph, self.airports, self.k = defaultdict(lambda: defaultdict(lambda: 0)), set(), len(tickets)
        for fr0m, to in tickets:
            self.graph[fr0m][to] += 1
            self.airports.add(fr0m)
            self.airports.add(to)
        self.airports = sorted(self.airports)
        return self.f('JFK', ('JFK',))

    def f(self, cur, path):
        if len(path) >= self.k + 1:
            return path
        for to in self.airports:
            if self.graph[cur][to] > 0:
                self.graph[cur][to] -= 1
                res = self.f(to, (*path, to))
                if res:
                    return res
                self.graph[cur][to] += 1
        return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
