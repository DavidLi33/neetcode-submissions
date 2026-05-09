class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}
        for letter in s:
            if letter not in dict_s:
                dict_s[letter] = 0
            dict_s[letter] += 1
        for letter in t:
            if letter not in dict_t:
                dict_t[letter] = 0
            dict_t[letter] += 1
        return dict_s == dict_t