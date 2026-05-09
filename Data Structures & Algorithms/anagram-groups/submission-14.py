class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            my_dict[sorted_s].append(s)
        result = []
        for key, value in my_dict.items():
            result.append(value)
        return result

