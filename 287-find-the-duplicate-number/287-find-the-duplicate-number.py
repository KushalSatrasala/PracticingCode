class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uni = set()
        for num in nums:
            if num in uni:
                return num
            uni.add(num)