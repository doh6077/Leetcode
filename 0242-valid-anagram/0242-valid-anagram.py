class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        dicts1, dicts2 ={}, {}
        for i in range(len(s)):
            dicts1[s[i]] = 1 + dicts1.get(s[i],0) # if the key doens't exist, it returns zero 
            dicts2[t[i]] = 1 + dicts2.get(t[i],0) # if the key doens't exist, it returns zero             
        for c in dicts1:
            if dicts1[c] != dicts2.get(c,0):
                return False 
        return True 
          


        