def oddEvenList(head):
    if head and head.next:
        odd = head
        even = start = odd.next
        while odd.next != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = start
    return head
