class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for string in strs:

            al = [0] * 26 

            for char in string:
                
              loc = ord(char) - ord("a")

              al[loc] += 1
            
            al = tuple(al)

            if al in anagrams.keys():
                anagrams[al].append(string)
            else:
                anagrams[al] = [string]
                
        return list(anagrams.values())