class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            #start of word after # delimeter
            i = j+1
            #one char past end of word since start of word + length
            j = i + length
            res.append(s[i:j])
            #move i also past end of word to repeat
            i = j
        return res