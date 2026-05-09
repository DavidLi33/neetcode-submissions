class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        for n in nums:
            my_dict[n] += 1
        arr = []
        for n, count in my_dict.items():
            arr.append([count, n])
        arr.sort()
        result = []
        while (k > 0):
            result.append(arr.pop()[1])
            k -= 1
        return result