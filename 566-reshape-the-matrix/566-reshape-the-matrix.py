class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        i = 0 
        j = 0
        
        if m == r and n == c:
            return mat
        
        if r * c != m * n:
            return mat
        
        ret = list()
        cur_list = list()
        k = 0
        while i < m:
            j = 0
            while j < n:
                if k == c:
                    ret.append(cur_list)
                    k = 0
                    cur_list = list()
                
                cur_list.append(mat[i][j])
                k += 1
                j += 1
            i += 1

        ret.append(cur_list)
        return ret