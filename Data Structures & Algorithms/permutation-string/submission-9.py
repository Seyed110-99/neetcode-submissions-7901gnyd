class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False 
        
        else:

            perm = [0 for _ in range(26)]

            for char in s1:
                x = ord(char) - ord("a")
                perm[x] += 1

            l = 0
            window = [0 for _ in range(26)]

            for r in range(len(s2)):
                
                x = ord(s2[r]) - ord("a")
                window[x] += 1
                
                if r - l + 1 == len(s1):
                    if window == perm:
                        return True
                    else:
                        p = ord(s2[l]) - ord("a")
                        window[p] -= 1
                        l += 1


            return False
            
            

