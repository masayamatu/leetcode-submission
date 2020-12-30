class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqnums = []
        for i in nums:
            sqnums.append(i*i)
            
        sqnums.sort()
        
        
        return sqnums