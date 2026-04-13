class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        word = ""
        n1 = len(word1)
        n2 = len(word2)

        longer = n1 if n1 > n2 else n2
        
        l = 0

        while l < longer:

            if l < n1 and l < n2:
                word += word1[l]
                word += word2[l]
            elif l >= n1:
                final = word + word2[l:]
                return final

            elif l>= n2:
                final = word + word1[l:]
                return final
            
            l += 1
        
        return word
            
