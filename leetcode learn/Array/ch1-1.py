class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 1
        temp = 2
        max = 0
        if not 1 in nums:
            return 0
        for i in nums:
            if i == 1 and i == temp:
                count += 1
                temp = i
            else:
                count = 1
                temp = i
            if count > max:
                max = count
        return max