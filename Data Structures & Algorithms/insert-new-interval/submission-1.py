class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # newInterval ends before curr interval starts
            # Place newInterval at spot and return
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # curr interval ends before newInterval starts
            # Append curr interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Overlap => Merge by expanding newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res