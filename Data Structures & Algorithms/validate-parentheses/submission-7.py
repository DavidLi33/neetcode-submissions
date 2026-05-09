class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {"}":"{", ")":"(", "]":"["}
        for paren in s:
            # If open parenthesis
            if paren not in my_dict:
                stack.append(paren)

            # If closed parenthesis
            else: 
                val = my_dict[paren]
                if not stack: 
                    return False
                if stack[-1] != val:
                    return False
                else:
                    stack.pop()
        return not stack
        

