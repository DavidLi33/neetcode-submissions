class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for w in strs:
            sorted_w = "".join(sorted(w))
            my_dict[sorted_w].append(w)
        result = []
        for key, value in my_dict.items():
            result.append(value)
        return result
