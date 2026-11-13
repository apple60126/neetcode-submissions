class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for nun in nums:
            if (nun - 1) not in nums:
                length = 1
                while (nun + length) in numsSet:
                    length +=1
                longest = max(length, longest)
        return longest