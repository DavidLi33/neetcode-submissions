class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {}
        for c in s1:
            dict_s1[c] = 1 + dict_s1.get(c,0)
        for i in range(len(s2)-len(s1)+1):
            s2_substr = s2[i:i+len(s1)]
            dict_s2 = {}
            for c in s2_substr:
                dict_s2[c] = 1 + dict_s2.get(c, 0)
            if dict_s1 == dict_s2:
                return True
        return False

            
        