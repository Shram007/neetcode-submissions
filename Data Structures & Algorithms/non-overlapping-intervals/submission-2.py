class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy (sort by start time)
        ''' intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res '''

        # Greedy (sort by end time)
        intervals.sort(key=lambda x:x[1])
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]
        return res