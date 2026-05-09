class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums = [-n for n in nums]
        heapq.heapify(new_nums)
        
        for i in range(k-1):
            heapq.heappop(new_nums)

        return -new_nums[0]