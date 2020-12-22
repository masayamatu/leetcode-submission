class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        characters = {')':'(','}':'{',']':'['}
        
        for i in s:
            if i in characters:
                top_element = stack.pop() if stack else '#'
                print(top_element)
                if characters[i] != top_element:
                    return False
            else:
                stack.append(i)
      
        return not stack