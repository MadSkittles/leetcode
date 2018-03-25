class Solution(object):
    def deleteNode(self, root, key):
        parent_node, node = None, root
        while node and node.val != key:
            parent_node = node
            if key < node.val:
                node = node.left
            else:
                node = node.right
        if not node:
            return root
        if not parent_node and not node.left and not node.right:
            return None
        else:
            self.f(parent_node, node)
            return root

    def f(self, parent_node, node):
        if not node.left and not node.right:
            if node == parent_node.left:
                parent_node.left = None
            else:
                parent_node.right = None
        elif node.left and not node.right:
            parnet_n, n = node, node.left
            while n.right:
                parnet_n = n
                n = n.right
            node.val = n.val
            self.f(parnet_n, n)
        else:
            parnet_n, n = node, node.right
            while n.left:
                parnet_n = n
                n = n.left
            node.val = n.val
            self.f(parnet_n, n)
