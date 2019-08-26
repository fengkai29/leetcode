class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        a = []
        intervals.sort()
        if intervals == []:
            return []
        if len(intervals) == 1:
            return intervals
        m = intervals[0]
        for i in range(len(intervals)-1):
            if intervals[i+1][0]>m[1]:
                a.append(m)
                m = intervals[i+1]
            if intervals[i+1][0]<=m[1] and intervals[i+1][1]>m[1]:
                m[1] = intervals[i+1][1]
            if i == len(intervals)-2:
                a.append(m)
        return a

a = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(Solution().merge(a))