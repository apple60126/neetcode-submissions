class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complete = 0
        for i in range(len(nums)):
            complete = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == complete:
                    return [i, j]
        return []


            


        