from common import TreeLinkNode


class Solution:
    def connect(self, root):
        head = root
        while head:
            p, head, tail = head, None, None
            while p:
                head = head or p.left or p.right
                tail = tail or p.left or p.right
                if p.left and tail != p.left:
                    tail.next = p.left
                    tail = tail.next
                if p.right and tail != p.right:
                    tail.next = p.right
                    tail = tail.next
                p = p.next


if __name__ == '__main__':
    solution = Solution()
    tree = TreeLinkNode.list2Tree([1, 2])
    solution.connect(tree)
    print(tree)
