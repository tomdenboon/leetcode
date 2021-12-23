def middleNode(head):
    size = 1
    node = head
    while node.next != None:
        node = node.next
        size += 1
    for _ in range(size//2):
        head = head.next
    return head
