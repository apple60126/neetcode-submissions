class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0
        for i in range(len(nums)):
            cnt = 0
            if nums[i] == 0: continue
            else:
                for j in range(i, len(nums)):
                    if nums[j] == 1:
                        cnt += 1
                    else: break
            max_cnt = max(max_cnt, cnt)
        return max_cnt



