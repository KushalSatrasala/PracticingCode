class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
        nums[:len(temp)] = temp
        nums[len(temp):] = [0 for _ in range(len(nums) - len(temp))]