class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1
        
        diff = len(s2) - len(s1) 
        for i in range(diff + 1):
            s2_substring = s2[i:i+len(s1)]
            s2_substring_dict = {}
            for char in s2_substring:
                s2_substring_dict[char] = s2_substring_dict.get(char, 0) + 1
            if s2_substring_dict == s1_dict:
                return True
        return False

            
        