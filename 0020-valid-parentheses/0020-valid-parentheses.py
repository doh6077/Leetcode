class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOPen[c]:
                    stack.pop()
                else:
                    return False 
        
        return True if not stack else False 
	
        