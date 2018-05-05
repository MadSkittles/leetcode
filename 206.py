from common import ListNode

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        p, next_p = head, head.next
        while next_p:
            next_next_p = next_p.next
            next_p.next = p
            p, next_p = next_p, next_next_p
        head.next=None
        return p

if __name__ == '__main__':
    solution=Solution()
    print(solution.reverseList(ListNode.list2ListNode([1,2,3])))
