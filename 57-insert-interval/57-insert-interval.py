class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        intLen = len(intervals)
        res_list = list()
        while i < intLen:
            j = i + 1
            cur_int = intervals[i]
            while j < intLen:
                next_int = intervals[j]
                if next_int[0] >= cur_int[0] and next_int[0] <= cur_int[1]:
                    cur_int[1] = max(cur_int[1], next_int[1])
                    j += 1
                else:
                    break
            
            res_list.append(cur_int)
            i = j
        
        return res_list