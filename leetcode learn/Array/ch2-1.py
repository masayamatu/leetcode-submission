class Solution:
    def shift(self,arr: List[int],temp):
        if temp == len(arr)-1:
            return 0     
        elif arr[temp] == 0:
            for i in range(len(arr)-1,temp+1,-1):
                arr[i] = arr[i-1]
            arr[temp+1] = 0
            if(temp+2 < len(arr)):
                self.shift(arr,temp+2)
            else:
                return 0
        else:
            self.shift(arr,temp+1)
    
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        self.shift(arr,0)