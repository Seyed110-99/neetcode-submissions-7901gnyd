class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        l = 0
        r = len(people) - 1
        boats = []

        boats = 0

        while l <= r:

            person1 = people[r]
            person2 = people[l]
            
            remain_cap = limit - person1
            
            if remain_cap >= person2:
                boats += 1
                l += 1
                r -= 1
            elif r == l:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1
            
        return boats

           