def reorderList(head):
    node = head
    nl = []
    l = 1
    while node.next:
        node = node.next
        nl.append(node)
        l += 1
    op = 0
    while op < l//2:
        last = nl.pop()
        last.next = head.next
        head.next = last
        head = last.next
        op += 1
    if l < 2:
        pass
    elif l % 2:
        head.next.next.next = None
    else:
        head.next.next = None
