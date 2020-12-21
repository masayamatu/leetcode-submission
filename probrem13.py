class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        if len(s) == 1:
            return roman[s]
        for i in range(0 , len(s)-1):
            if(roman[s[i]] < roman[s[i+1]]):
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        result += roman[s[len(s)-1]]
        return result