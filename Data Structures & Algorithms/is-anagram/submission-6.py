class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use defaultdict(int) to set a default value of 0
        if len(s) != len(t):
            return False
        dict1, dict2 = defaultdict(int), defaultdict(int)
        for c1 in s:
            dict1[c1] += 1
        for c2 in t:
            dict2[c2] += 1
        return dict1 == dict2
