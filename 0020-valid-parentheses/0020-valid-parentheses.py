class Solution:
    def isValid(self, s: str) -> bool:
        tokens = {'(':')','[':']','{':'}'}
        stack = [] 

        def isMatch(openTerm, closeTerm):
            return tokens[openTerm] == closeTerm 
        
        for i in s:
            if i in tokens:
                print(i)
                stack.append(i)
            else:
                if len(stack) == 0 or not isMatch(stack.pop(), i):
                    return False 
        
        return not stack 