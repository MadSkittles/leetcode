class Trie:
    class _Node:
        def __init__(self, val):
            self.val = val
            self.children = {}

    def __init__(self):
        self.root = Trie._Node(None)

    def insert(self, word):
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                new_node = Trie._Node(c)
                cur_node.children[c] = new_node
                cur_node = new_node
        cur_node.children[None] = None

    def search(self, word):
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        return None in cur_node.children

    def startsWith(self, prefix):
        cur_node = self.root
        for c in prefix:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        return True
