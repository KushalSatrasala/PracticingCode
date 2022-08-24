class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        slen = len(nums)
        buckets = [None for _ in range(slen + 1)]

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        for key in freq.keys():
            val = freq[key]
            if buckets[val] is None:
                buckets[val] = (list(), 0)
            
            lt, cnt = buckets[val]
            lt.append(key)
            buckets[val] = (lt, cnt + 1)
        
        i = slen
        cur_count = 0
        res_list = list()
        while i >= 0:
            if buckets[i] != None:
                lt, cnt = buckets[i]
                cur_count += cnt
                res_list.extend(lt)
            
            if cur_count >= k:
                break
            i -= 1
        
        return res_list
                
        