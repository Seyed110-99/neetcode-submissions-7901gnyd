class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        boats = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            p1 = people[r]
            p2 = people[l]
            

            if p1 + p2 <= limit:
                boats += 1
                l += 1
                r -= 1

            else:
                r -= 1
                boats += 1

        return boats
            

        

           