class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        #[[5,0], [3,1], [4,2]]
        A.sort()

        l, r = 0, len(nums) - 1
        curr = 0
        while l < r: 
            curr = A[l][0] + A[r][0]
            if curr == target:
                return sorted([A[l][1], A[r][1]])
            if curr > target:
                r -= 1
            else:
                l += 1
        return []


            


        