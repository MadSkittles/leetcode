class Solution:
    def networkDelayTime(self, times, N, K):
        graph = {}
        for u, v, w in times:
            graph.setdefault(u, []).append((v, w))
        dis = [0] + [float('inf') if i != K else 0 for i in range(1, N + 1)]
        s, e, cur_node = {K}, {i for i in range(1, N + 1) if i != K}, K
        while e:
            for v, w in graph.get(cur_node, []):
                dis[v] = min(dis[v], dis[cur_node] + w)
            min_dis, min_node = float('inf'), None
            for node in e:
                if dis[node] < min_dis:
                    min_dis, min_node = dis[node], node
            if min_node is None:
                return -1
            e.remove(min_node)
            s.add(min_node)
            cur_node = min_node
        return max(dis)