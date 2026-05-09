class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        #initialize empty hashmaps to store characters in T and window
        countT, window = {}, {}
        #store required letters that we need from T
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        #res stores left, right pointer
        res, resLen = [-1,-1], float("infinity")
        l= 0
        for r in range(len(s)):
            #current char
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                #pop from left until condition isn't met (have != need)
                #decreases count of char on the left by one in the window hashmap
                window[s[l]] -= 1
                #if removing the character causes window count of left char to be less than have count
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        #extract final left and right values
        l, r = res
        #if no result exists
        if resLen == float("infinity"):
            return ""
        else:
            return s[l:r+1] 
        
        
        