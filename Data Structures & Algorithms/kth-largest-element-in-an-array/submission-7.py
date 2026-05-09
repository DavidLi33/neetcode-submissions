class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Creates max heap
        new_nums = [-n for n in nums]
        heapq.heapify(new_nums)
        
        # Pop k values
        for i in range(k-1):
            heapq.heappop(new_nums)

        # Returns kth largest value
        return -new_nums[0]