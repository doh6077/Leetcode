class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#        return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        ptr1, ptr2 = 0, 0 
        result = {}
        for i, v in enumerate(s):
            result[v] = s.count(v)
        for j, v2 in enumerate(t):
            
            if v2 not in result:
            # this means t has a character that s doesn't have
                return False
            else:
                count_res  = t.count(v2)
                if count_res != result[v2]:
                    return False
        return True 




          


        