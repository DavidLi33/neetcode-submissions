class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s, dict_t = defaultdict(int), defaultdict(int) 
        for c1 in s:
            dict_s[c1]+=1;
        for c2 in t:
            dict_t[c2]+=1;
        return dict_s == dict_t
