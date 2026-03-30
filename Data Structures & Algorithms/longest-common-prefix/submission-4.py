class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        long_prefix = ""
        
        word = strs[0]

        for i in range(len(word)):

            char = word[i]

            for words in strs[1:]:

                if len(words) > i:

                    if char != words[i]:

                        return long_prefix
                else:
                    return long_prefix
            long_prefix += char 

            print(long_prefix)
        return long_prefix



                