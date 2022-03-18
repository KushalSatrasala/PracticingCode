class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res_list = list()
        i = 0
        while i < (rowIndex + 1):
            cur_list = list()
            j = 0 
            while j < i:
                sum = 0 
                if j - 1 >= 0:
                    sum += res_list[i - 1] [j - 1]
                sum += res_list[i - 1] [j]
                cur_list.append(sum)
                j += 1
            cur_list.append(1)
            res_list.append(cur_list)
            i += 1
        
        return res_list[rowIndex]