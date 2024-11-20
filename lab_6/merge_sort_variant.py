# This is MergeSort for a linked list.
# =====================================
# - Converts an array to a linked list for sorting.
# - Splits the list into two halves using a slow/fast pointer technique.
# - Recursively sorts each half.
# - Merges the sorted halves back into a single sorted list.
# --------------------------------------------------------------
# Tracks time, comparisons, and copy operations as required by the task.

from performance_metrics import PerformanceMetrics

# structure for linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    head = ListNode(arr[0]) if arr else None
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

def merge_sort_linked_list(head, metrics=None):
    import time

    if metrics is None:
        metrics = PerformanceMetrics()

    start_time = time.perf_counter()

    # find the middle of the linked list
    def get_middle(head):
        if not head:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            metrics.comparisons += 1  # track comparisons
            slow = slow.next
            fast = fast.next.next

        return slow

    # merge two sorted linked lists
    def merge(left, right):
        dummy = ListNode()
        tail = dummy

        while left and right:
            metrics.comparisons += 1
            if left.val <= right.val:
                tail.next = left
                metrics.copy_operations += 1
                left = left.next
            else:
                tail.next = right
                metrics.copy_operations += 1
                right = right.next
            tail = tail.next

        tail.next = left or right  # attach the remaining part
        return dummy.next

    # recursive MergeSort for linked list
    def merge_sort(head):
        if not head or not head.next:  # base case: single element or empty
            return head

        middle = get_middle(head)  # split the list
        next_to_middle = middle.next
        middle.next = None

        left = merge_sort(head)
        right = merge_sort(next_to_middle)

        return merge(left, right)

    sorted_head = merge_sort(head)

    metrics.time_elapsed = time.perf_counter() - start_time
    return sorted_head, metrics