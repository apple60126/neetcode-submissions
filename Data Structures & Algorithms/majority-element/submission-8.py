from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sorted(count.items(), key = lambda x:x[1], reverse = True)[0][0]
            
        