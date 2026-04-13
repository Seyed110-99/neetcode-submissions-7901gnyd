class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        word = ""
        n1 = len(word1)
        n2 = len(word2)

        longer = max(len(word1), len(word2))
        
        l = 0

        while l < longer:

            if l < n1:
                word += word1[l]
            if l < n2:
                word += word2[l]
            
            l += 1
        
        return word
            
