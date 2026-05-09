class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {")":"(", "]":"[", "}":"{"}
        #Implement stack as a list
        stack = []

        for char in s:
            #If char is a closed parenthesis
            if char not in my_map:
                stack.append(char)
                continue
            #If char is an open parenthesis
            if not stack or stack[-1] != my_map[char]:
                return False
            #Match made between left and right
            stack.pop()
        
        return not stack
            

