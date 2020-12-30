class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        thridnum = 0
        count = 0
        temp = -1
        nums.sort()
        if(len(nums)<3):
            return nums[len(nums)-1]
        firstnum = nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
            if (firstnum > nums[i]) and temp != nums[i]:
                count += 1
                temp = nums[i]
                if count == 2:
                    thirdnum = nums[i]
                    return thirdnum
        if count < 2:
            return nums[len(nums)-1]