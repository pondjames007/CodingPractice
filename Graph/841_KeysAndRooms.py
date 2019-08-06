# TIPS:
# Do DFS from start point

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        visited[0] = True
        
        self.lookup(rooms, 0, visited)
        
        return all(visited)
    
    def lookup(self, rooms, pos, visited):
        if not rooms[pos]: return
        
        for nxt in rooms[pos]:
            if not visited[nxt]:
                visited[nxt] = True
                self.lookup(rooms, nxt, visited)
        
        return
        