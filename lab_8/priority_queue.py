import heapq

class PriorityQueue:
    # priority queue (min-heap)

    def __init__(self):
        self._heap = []

    def push(self, item):
        # add item to queue
        heapq.heappush(self._heap, item)

    def pop(self):
        # remove and return highest priority item
        # return None if empty
        if not self._heap:
            return None
        return heapq.heappop(self._heap)

    def peek(self):
        # return highest priority item without removing
        if not self._heap:
            return None
        return self._heap[0]

    def is_empty(self):
        # return True if queue is empty
        return len(self._heap) == 0

    def size(self):
        # return number of items
        return len(self._heap) 