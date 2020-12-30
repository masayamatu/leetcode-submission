class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increase = True
        if len(arr) == 1:
            return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] > arr[i+1]:
                if i == 0:
                    return False
                increase = False
            elif increase == False and arr[i] < arr[i+1]:
                return False
        if increase == True:
            return False
        return True