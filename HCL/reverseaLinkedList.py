def reversingLinkedList(head):
    if head is None or head.next is None:
        return head

    rest = reversingLinkedList(head.next)

    head.next.next = head
    head.next = None

    return rest




