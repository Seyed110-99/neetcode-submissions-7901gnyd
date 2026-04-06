class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for string in strs:

            al = [0] * 26 

            for char in string:
                
              loc = ord(char) - ord("a")

              al[loc] += 1
            
            al = tuple(al)
            anagrams[al].append(string)

            # if al in anagrams:
            #     anagrams[al].append(string)
            # else:
            #     anagrams[al] = [string]

        return list(anagrams.values())