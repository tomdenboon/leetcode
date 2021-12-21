class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    l3 = ListNode((l1.val + l2.val) % 10)
    next_l3 = l3
    if l1.val + l2.val >= 10:
        n = 1
    else:
        n = 0
    while l1.next or l2.next or n:
        v1 = 0
        v2 = 0
        if l1.next:
            l1 = l1.next
            v1 = l1.val
        if l2.next:
            l2 = l2.next
            v2 = l2.val
        new = (v1 + v2 + n) % 10
        next_l3.next = ListNode(new)
        next_l3 = next_l3.next
        if v1 + v2 + n >= 10:
            n = 1
        else:
            n = 0
    return l3
