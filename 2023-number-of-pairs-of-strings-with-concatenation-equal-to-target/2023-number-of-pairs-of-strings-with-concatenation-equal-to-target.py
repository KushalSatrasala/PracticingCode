class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        lookup = dict()
        pairs = 0
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = list()
            lookup[num].append(i)
        
        t_len = len(target)
        i = 0
        
        while i < t_len:
            left = target[:i]
            right = target[i:]
            if left in lookup and right in lookup:
                if left == right:
                    lt = len(lookup[left])
                    pairs += lt * ( lt - 1 )
                else:
                    lc = len(lookup[left])
                    rc = len(lookup[right])
                    pairs += (lc * rc)
            i += 1
        
        return pairs
            