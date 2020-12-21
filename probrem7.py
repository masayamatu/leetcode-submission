import sys

class Solution:
    def reverse(self, x: int) -> int:
        
        if (x >= 2 ** 31 -1) or ( x <= -2 ** 31):
            return 0
        
        elif x > 0:
            a = int(str(x)[::-1])
            if a >= 2 ** 31 -1:
                return 0
            else:
                return a
             
        elif x <= 0:
            a = -1 * int(str(x*-1)[::-1])
            if a <= -2 ** 31:
                return 0
            else:
                return a
            