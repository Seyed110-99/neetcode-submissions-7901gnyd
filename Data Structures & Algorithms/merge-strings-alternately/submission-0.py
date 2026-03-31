class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        string = ""
        adding = True
        w1 = 0
        w2 = 0
        while adding:
            
            if w1 < len(word1):
               string += word1[w1]
               w1 += 1
            if w2 < len(word2):
                string += word2[w2]
                w2 += 1
            else:
                adding = False

        if w1 >= len(word1):
            string += word2[w2:]
        if w2 >= len(word2):
            string += word1[w1:]
        return string
