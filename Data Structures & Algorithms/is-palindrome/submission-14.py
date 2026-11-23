class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        ch_s = "".join(ch.lower() for ch in s if ch.isalnum()) 
        r = len(ch_s) - 1

        print(ch_s, r)
        while l <= r:
            print(l, r)
            if ch_s[l] == ch_s[r]:
                l += 1
                r -= 1
                
            else:
                return False
        return True