class WordDictionary:
    class _Node:
        def __init__(self, val):
            self.val = val
            self.children = {}

        def __str__(self):
            return self.val

        __repr__ = __str__

    def __init__(self):
        self.root = WordDictionary._Node(None)

    def addWord(self, word):
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                new_node = WordDictionary._Node(c)
                cur_node.children[c] = new_node
                cur_node = new_node
        cur_node.children[None] = None

    def search(self, word):
        nodes = [self.root]
        for c in word:
            next_nodes = []
            for cur_node in nodes:
                if cur_node is None:
                    continue
                else:
                    if c in cur_node.children:
                        next_nodes.append(cur_node.children[c])
                    elif c == '.':
                        next_nodes.extend(cur_node.children.values())
            nodes = next_nodes
        return any(None in n.children for n in nodes if n)
