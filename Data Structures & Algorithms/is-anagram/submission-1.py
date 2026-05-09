class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort_s = "".join(sorted(s))
        # sort_t = "".join(sorted(t))
        # return sort_s == sort_t
        if len(s)!= len(t):
            return False

        dictS, dictT = {}, {}
        for i in range (len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
        return dictS == dictT
