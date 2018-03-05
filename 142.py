from common import ListNode

class Solution(object):
    def detectCycle(self, head):
        p, vistied = head, set()
        while p and p not in vistied:
            vistied.add(p)
            p = p.next
        return p