class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        frequency_s = {}
        for x in s:
            if x not in frequency_s:
                frequency_s[x] = 1
            else:
                frequency_s[x] += 1

        frequency_t = {}
        for y in t:
            if y not in frequency_t:
                frequency_t[y] = 1
            else:
                frequency_t[y] += 1

        return frequency_s == frequency_t
        