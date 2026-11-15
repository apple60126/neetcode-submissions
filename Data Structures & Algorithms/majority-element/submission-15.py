from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return sorted(cnt, key = cnt.get, reverse = True)[0]

            
        