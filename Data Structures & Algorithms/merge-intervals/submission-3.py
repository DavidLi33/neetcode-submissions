class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for s, e in intervals[1:]:
            last_end = res[-1][1]
            if s <= last_end:
                res[-1][1] = max(last_end, e)
            else:
                res.append([s, e])
        return res
        