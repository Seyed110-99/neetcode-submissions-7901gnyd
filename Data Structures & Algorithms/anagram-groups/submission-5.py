class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_w = defaultdict(list)

        for word in strs:

            f = [0] * 26

            for char in word:
                x = ord(char) - ord("a")
                f[x] += 1

            f = tuple(f)
            dict_w[f].append(word)

        return list(dict_w.values())
            