class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Stores array values and size
        self.minHeap, self.k = nums, k
        # Converts minHeap from array => heap
        heapq.heapify(self.minHeap)
        # Pop from heap to ensure that size is as large as k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add value to heap
        heapq.heappush(self.minHeap, val)
        # Adjust heap if size is exceeded
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Return top value of heap => kth largest integer
        return self.minHeap[0]
        
