from src.model import ListNode


def merge_two_lists(l1: ListNode, l2: ListNode):
    dummy = ListNode()
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    if l1:
        cur.next = l1
    if l2:
        cur.next = l2

    return dummy.next
