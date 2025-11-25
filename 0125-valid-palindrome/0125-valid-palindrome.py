import re
# two pointers 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(cleaned_s)
        left, right = 0, n -1
        while left < right: 
        
            if cleaned_s[left] == cleaned_s[right]:
                left += 1 
                right -= 1
            else:
                print(left,right)
                print(s[left], s[right])
                return False 
        
        return True
        