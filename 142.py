from common import ListNode


class Solution(object):
    def detectCycle(self, head):
        p, fast_p = head, head
        while p and fast_p:
            p, fast_p = p.next, fast_p.next.next if fast_p.next else fast_p.next
            if p == fast_p != None:
                break
        else:
            return None
        p = head
        while p != fast_p:
            p, fast_p = p.next, fast_p.next
        return p
