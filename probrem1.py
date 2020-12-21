class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = {}
        
        for i , num in enumerate(nums):
            n = target - num
            
            if n not in ans:
                ans[num] = i
            else:
                return [ans[n],i]