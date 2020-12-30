import copy
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedheights = copy.copy(heights)
        sortedheights.sort()
        count = 0
        
        for i in range(len(heights)):
            if sortedheights[i] != heights[i]:
                count += 1
                
        return count