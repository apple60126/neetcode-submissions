class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #dic's key is random
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0) # if you see a num for the first time and not yet exist in the key yet, count[num] += 1 will error. count.get(num, 0) syntax dict.get(key, default=None) if for the first time, it will default to 0 and increment by 1
        for num, count in count.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res