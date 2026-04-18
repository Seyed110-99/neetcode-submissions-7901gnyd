class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        longest = 0

        for r in range(len(s)):

            freq = {}
            
            for i in range(l, r+1):
                
                freq[s[i]] = freq.get(s[i], 0) + 1

            if (r - l + 1) - max(freq.values()) <= k:
                
                longest = max(longest, (r - l + 1))

            else:
                l += 1

        return longest
            
        


        


        