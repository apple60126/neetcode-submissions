class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0
        for num in nums:
            print(num)
            if num == 0:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
                print(max_cnt, cnt)
            else: cnt += 1
            print(cnt)
        return max(max_cnt, cnt)
        



