class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        low = 0
        high = n-1
        while low < high:
            val = numbers[low] + numbers[high]
            if val < target:
                low += 1
            elif val > target:
                high -= 1
            else:
                return [low+1, high+1]
        return []