class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        # For each number make a new perm
        for n in nums:
            new_perms = []
            # For each existing permutation
            for p in perms:
                # Try to put n at every position in the existing permutations
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms