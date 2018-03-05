from common import UndirectedGraphNode


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        map = {node: UndirectedGraphNode(node.label)}
        q=[node]
        while q:
            next_q=[]
            for cur_node in q:
                for n in cur_node.neighbors:
                    if n not in map:
                        new_node = UndirectedGraphNode(n.label)
                        map[n]=new_node
                        next_q.append(n)
                    else:
                        new_node = map[n]
                    map[cur_node].neighbors.append(new_node)
            q=next_q
        return map[node]
