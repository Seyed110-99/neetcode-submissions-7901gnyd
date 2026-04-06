class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        f = [0] * 26

        for char in s:

            p = ord(char) - ord("a")

            f[p] += 1
        
        for char in t:

            p = ord(char) - ord("a")

            f[p] -= 1
        
        for x in f:
            if x != 0:
                return False
        return True