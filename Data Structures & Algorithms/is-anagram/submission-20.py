from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = {}
        if len(s) != len(t): return False
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        for c in t:
            cnt[c] = cnt.get(c, 0) - 1
            if cnt[c] < 0:
                return False     
        return True   