class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = ''
        
        x = str(x)
        y = x[::-1]
        
        for i in range(0,len(x)):
            if x[i] != y[i]:
                return 0
                break
        return 'true'
