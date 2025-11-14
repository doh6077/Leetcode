# set에 저장하면서 중복 여부 확인하기

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for v in nums:
            if v in seen:
                return True
            seen.add(v)
        return False






        