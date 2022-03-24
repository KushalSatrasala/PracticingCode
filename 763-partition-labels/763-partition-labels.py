class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_dict = dict()
        
        for index,ch in enumerate(s):
            if ch not in char_dict:
                char_dict[ch] = [index, index]
            start, end = char_dict[ch][0], char_dict[ch][1]
            char_dict[ch] = [start, index]
        
        intervals = sorted(char_dict.values(), key=lambda a: a[0])
        
        merge_list = list()
        mergeLen = len(intervals)
        i = 0
        while i < mergeLen:
            cur_intr = intervals[i]
            j = i + 1
            while j < mergeLen and (intervals[j][0] > cur_intr[0] and intervals[j][0] < cur_intr[1]):
                cur_intr[1] = max(cur_intr[1], intervals[j][1])
                j += 1
            merge_list.append(cur_intr)
            i = j
        
        res_list = list()
        for lst in merge_list:
            res_list.append(lst[1] - lst[0] + 1)

        return res_list
            