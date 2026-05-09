class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num] += 1
        arr = []
        for num, count in my_dict.items():
            arr.append([count, num])
        arr.sort()
        res = []
        while (k > 0):
            res.append(arr.pop()[1])
            k -= 1
        return res