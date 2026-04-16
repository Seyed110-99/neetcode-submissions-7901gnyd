class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        boats = 0

        l = 0
        r = len(people) - 1

        while l <= r:

            add = people[l] + people[r]

            if add <= limit:

                boats += 1
                l += 1

            elif people[r] <= limit:

                boats += 1

            else:

                boats += 1
                l -= 1

            r -= 1
        
        return boats
        

           