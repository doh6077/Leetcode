class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res =""

        for i in range(len(strs[0])):
            for j in strs:
                if len(j) == i or strs[0][i] != j[i]:
                    return res 
            
            res += strs[0][i]
        return res