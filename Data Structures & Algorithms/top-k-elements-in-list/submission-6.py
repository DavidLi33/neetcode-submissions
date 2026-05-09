class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = 1 + my_dict.get(num, 0)
        
        lists = []
        for num, count in my_dict.items():
            lists.append([count, num])
        lists.sort() 

        res = []
        while k > 0:
            res.append(lists.pop()[1])
            k -= 1
        return res