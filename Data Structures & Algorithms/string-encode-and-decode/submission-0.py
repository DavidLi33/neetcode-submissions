class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):           #s = 4#neet4#code4#love3#love
            j = i                   #starts at 0
            while s[j] != '#':      #j goes from 0 => 1
                j += 1                  
            length = int(s[i:j])    #retrieve length of string
            i = j + 1               #i = 2 (start of string)
            j = i + length          #j = 2+4 = 6
            res.append(s[i:j])      #appends s[2:6] = neet
            i = j                   #i = 6  
            
        return res