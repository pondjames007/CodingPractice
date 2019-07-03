from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets: return []
        
        itineraries = defaultdict(list)
        # Get ticket dictionary, 0 -> not visit yet, 1 -> visited
        for f, t in tickets:
            itineraries[f].append([t, 0])

        # to make sure it is in lexical order, and the returned answer will be assured to be the smallest lexical order
        # because the smaller lexical order element will be searched first, and if there is an answer, it must be the smallest.
        for f, _ in tickets:
            itineraries[f].sort()
        
        return self.find('JFK', len(tickets), itineraries) # the total "indexes" must be len(tickets) (the answer length is len(tickets)+1)

    def find(self, pos, length, itineraries):
        if not length: return [pos] # if length == 0 then return the position right now (do not need to go further)(and it also means that you have used every tickets)
        if pos not in itineraries: return [] # if you don't have the ticket from the pos, return [] to represent wrong answer
        
        for i in range(len(itineraries[pos])): # go through every possible destinations
            if itineraries[pos][i][1] == 1: continue # if it is visited, skip
                
            itineraries[pos][i][1] = 1 # set the destination to be visited
            route = self.find(itineraries[pos][i][0], length-1, itineraries) # go to the destination and find next destination
            
            if route: return [pos] + route # if the route is returned with value: add it with the pos right now
            
            itineraries[pos][i][1] = 0 # if there is no answer, reset the destination status
        
        return [] # if no answer after going through all destinations, return []