class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        ans = ''
        
        strs = sorted(strs)
        
        for i in strs[0]:
            if strs[-1].startswith(ans+i):
                ans += i
            else:
                break
        
        return ans