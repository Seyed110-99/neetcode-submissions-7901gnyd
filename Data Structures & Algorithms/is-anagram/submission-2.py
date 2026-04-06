class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        lst1 = {}
        lst2 = {}

        for char in s:
            lst1[char] = lst1.get(char, 0) + 1

        for char in t:
            lst2[char] = lst2.get(char, 0) + 1

        if lst1.keys() == lst2.keys():

            for key in lst1.keys():

                if lst1[key] != lst2[key]:
                    return False
            
            return True
            
        else:
            return False