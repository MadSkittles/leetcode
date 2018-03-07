class BSTIterator(object):
    def __init__(self, root):
        self.cur_node = root
        self.stack = []
        while self.cur_node and self.cur_node.left:
            self.stack.append(self.cur_node)
            self.cur_node = self.cur_node.left

    def hasNext(self):
        return self.cur_node is not None

    def next(self):
        val = self.cur_node.val
        if self.cur_node.right:
            self.cur_node = self.cur_node.right
            while self.cur_node.left:
                self.stack.append(self.cur_node)
                self.cur_node = self.cur_node.left
        else:
            while len(self.stack) > 0 and self.cur_node == self.stack[-1].right:
                parent_node = self.stack.pop()
                self.cur_node = parent_node
            if len(self.stack) == 0:
                self.cur_node = None
            else:
                parent_node = self.stack.pop()
                self.cur_node = parent_node
        return val
