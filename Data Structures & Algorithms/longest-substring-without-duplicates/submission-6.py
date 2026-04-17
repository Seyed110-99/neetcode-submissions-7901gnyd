class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        length = 0
        l = 0 

        for r in range(len(s)):
            
            
            while s[r] in characters:
                print(characters, s[r], s[l])
                characters.remove(s[l])
                l += 1

            characters.add(s[r])
            
            length = max(length, r - l + 1)   
                    
        return length
                
