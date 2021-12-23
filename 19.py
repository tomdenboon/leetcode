def removeNthFromEnd(head, n):
    size = 1
    node = head
    remove_head = node
    while node.next != None:
        if size > n:
            remove_head = remove_head.next
        node = node.next
        size += 1
    if remove_head.next == None:
        return None
    if size == n:
        return remove_head.next
    remove_head.next = remove_head.next.next
    return head
