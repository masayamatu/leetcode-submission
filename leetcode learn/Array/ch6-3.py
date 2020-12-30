class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        daNum = []
        nums.sort()
        now = 1
        i = 0
        if len(nums) == 0:
            return nums
        while i<len(nums) and now <= len(nums):
            print(nums[i],now)
            if nums[i] == now:
                now += 1
                i += 1
            elif nums[i] != now:
                if now-1 == nums[i]:
                    if i == len(nums)-1:
                        daNum.append(now)
                        i += 1
                        continue
                    i += 1
                elif now != nums[i]:
                    daNum.append(now)
                    now += 1
                
        
        if  len(nums) != nums[len(nums)-1] and len(nums) not in daNum:
            daNum.append(len(nums))

        return daNum