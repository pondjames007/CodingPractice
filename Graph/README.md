# Graph

## Concepts
* Graph Problems 相對簡單 基本上都不脫模板只是需要一點點變化而已

* String Comparison: it will compare character by character, if will compare until two characters has the answer (not equal)
* Graph Problem Template: **Graph Coloring**: Color a node as red, and all its neighbors as blue recursively. If there is any conflicts the the graph is not bipartie. Use DFS/BFS -> [#886](./886_PossibleBipartition.py)
* Classic BFS Template -> [#934](./934_ShortestBridge.py)
```
    dirs = [0, 1, 0, -1, 0]
    while not q.empty():
        size = q.qsize()
        while size:
            size -= 1 # 按層擴展 size是當前這層需要擴展的節點數量
            x, y = q.get()
            for i in range(4):
                # use 1d array to describe 2d 4 directions
                tx = x + dirs[i]
                ty = y + dirs[i+1]
                if tx < 0 or ty < 0 or tx >= len(A[0]) or ty >= len(A) or A[ty][tx] == 2: continue
                if A[ty][tx] == 1: return steps
                A[ty][tx] = 2
                q.put((tx, ty))
        steps += 1
```
* use queue: import queue
    * queue.Queue(), queue.PriorityQueue()
    * q.put(), q.get() -> push, pop
    * q.qsize() -> get length
    * it is an object, cannot iterate to see the value

* use 1d array to describe 2d 4 directions
```
    dirs = [0, 1, 0, -1, 0]
    for i in range(4):      
        tx = x + dirs[i]
        ty = y + dirs[i+1]
```
* a = 1 or 0, use 1 - a to change state between 1 and 0
* list initialization: if the initialization is mutable, use for loop to do initialization.

## Problems

### Easy

* [No. 690 Employee Importance](./690_EmployeeImportance.py) --- [Solution Video](https://www.youtube.com/watch?v=kK9TBtQBmCg&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=29)
* [No. 733 Flood Fill](./733_FloodFill.py) --- [Solution Video](https://www.youtube.com/watch?v=ln_mc5LtL5M&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=26)

### Medium

* [No. 332 Reconstruct Itinerary](./332_ReconstructItinerary.py) --- [Solution Video](https://www.youtube.com/watch?v=4udFSOWQpdg&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=35)
* [No. 200 Number of Islands](../Search/200_NumberOfIslands.py) --- In [Search](../Search)
* [No. 547 Friend Circles](../Search/547_FriendCircles.py) --- In [Search](../Search)
* [No. 684 Redundant Connection](./684_RedundantConnection.py) --- [Solution Video](https://www.youtube.com/watch?v=4hJ721ce010&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=30)
* [No. 207 Course Schedule](./207_CourseSchedule.py) --- [Solution Video](https://www.youtube.com/watch?v=M6SBePBMznU&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=27)
* [No. 399 Evaluate Division](./399_EvaluateDivision.py) --- [Solution Video](https://www.youtube.com/watch?v=M6SBePBMznU&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=25)
* [No. 743 Network Delay Time](./743_NetworkDelayTime.py) --- [Solution Video](https://www.youtube.com/watch?v=M6SBePBMznU&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=24)
* [No. 959 Regions Cut By Slashes](./959_RegionsCutBySlashes.py)  --- [Solution Video](https://www.youtube.com/watch?v=n3s9Q7GtfB4&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=5)
* [No. 210 Course Schedule II](./210_CourseScheduleII.py) --- [Solution Video](https://www.youtube.com/watch?v=x1wXkRrpavw&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=21)
* [No. 787 Cheapest Flight within K Stops](../Search/787_CheapestFlightKStops.py) --- In [Search](../Search)
* [No. 817 Linked List Components](../LinkedList/817_LinkedListComponents.py) --- In [Linked List](../LinkedList)
* [No. 841 Keys and Rooms](./841_KeysAndRooms.py) --- [Solution Video](https://www.youtube.com/watch?v=x1wXkRrpavw&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=14)
* [No. 863 All Nodes Distance K in Binary Tree](./863_AllNodesDistanceKInBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=x1wXkRrpavw&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=12)
* [No. 802 Find Eventual Safe States](./802_FindEventualSafeState.py) --- [Solution Video](https://www.youtube.com/watch?v=x1wXkRrpavw&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=19)
* [No. 886 Possible Bipartition](./886_PossibleBipartition.py) --- [Solution Video](https://www.youtube.com/watch?v=x1wXkRrpavw&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=9)
* [No. 934 Shortest Bridge](./934_ShortestBridge.py) --- [Solution Video](https://www.youtube.com/watch?v=JU-g1mNUaSE&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=9)
* [No. 417 Pacific Atlantic Water Flow](../Search/417_PacificAtlanticWaterFlow.py) --- In [Search](../Search)
* [No. 1129 Shortest Path with Alternating Colors](./1129_ShortestPathWithAlternatingColors.py) --- [Solution Video](https://www.youtube.com/watch?v=ZobIimNrSFA&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=2)

### Hard

* [No. 675 Cut Off Trees for Golf Event](../Greedy/675_CutOffTrees.py) --- In [Greedy](../Greedy)
* [No. 685 Redundant Connection II](./685_RedundantConnectionII.py) --- [Solution Video](https://www.youtube.com/watch?v=lnmJT5b4NlM&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=29)
