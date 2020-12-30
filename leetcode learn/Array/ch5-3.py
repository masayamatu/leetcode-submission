class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        for i in range(len(nums)):
            if nums[i] != 0:
                point = i
                while nums[point-1] == 0 and point >= 1:
                    nums[point],nums[point-1] = nums[point-1],nums[point]
                    point -= 1
        
        return nums