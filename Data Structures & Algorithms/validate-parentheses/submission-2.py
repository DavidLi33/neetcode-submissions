class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char not in my_map:
                stack.append(char)
                continue
            if len(stack) == 0 or stack[-1] != my_map[char]:
                return False
            stack.pop()

        return not stack