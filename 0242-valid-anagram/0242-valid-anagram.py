class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts1 = {} 
        dicts2 = {} 
        for i in range(len(s)):
            if s[i] not in dicts1:
                dicts1[s[i]] = 1 
            else:
                dicts1[s[i]] += 1 
             
        for i in range(len(t)):
            if t[i] not in dicts2:
                dicts2[t[i]] = 1 
            else:
                dicts2[t[i]] += 1   
        return dicts1 == dicts2
          


        