class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # j now at # position after length, i at position before length
            length = int(s[i:j])
            # i now at start of word
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
