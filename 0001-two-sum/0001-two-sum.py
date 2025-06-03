class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sortednums = sorted(nums)
        l, r = 0, len(sortednums) -1
        answers = []
        while l < r:

            if sortednums[r] + sortednums[l] > target:
                r -= 1
            elif sortednums[r] + sortednums[l] < target:
                l += 1
            else:
                answers.append(nums.index(sortednums[r]))

                if sortednums[r] == sortednums[l]:
                    answers.append(nums.index(sortednums[l], nums.index(sortednums[r]) + 1,len(nums)))
                else:
                    answers.append(nums.index(sortednums[l]))
                
                break
        return answers

                








