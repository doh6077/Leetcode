class Solution:
    def romanToInt(self, s: str) -> int:
        nums = 0 
        letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}
        for index, char in enumerate(s):
            if index != len(s) -1:
                nextl = s[index+1]
                if letters.get(nextl) > letters.get(char):
                    nums -= letters.get(char)
                else: 
                    nums += letters.get(char)
            else: 
                nums += letters.get(char)
        
        return nums 


        