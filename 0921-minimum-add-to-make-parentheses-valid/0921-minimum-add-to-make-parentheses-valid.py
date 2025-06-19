class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = [] 
        token = {"(":")"}
        count = 0 

        for i in s:
            # check if it is open term 
            if i in token:
                stack.append(i)
            else:
                if len(stack) != 0:
                    stack.pop()
                    
                else:
                    count += 1 
        return count + len(stack)