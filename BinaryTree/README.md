# Binary Tree

## Concepts
* [Trie](https://zh.wikipedia.org/wiki/Trie) -> [#208](./208_ImplementTrie.py)
    用空間換時間
    多層的hash table
    每一層每一級key的長度都是1
    在每個節點標記是不是在字典裡
    應用不多 特殊場合很高效

* 2D list initialization: [[""] * w for _ in range(h)]
    **wrong way**: [[""] * w] * h -> this will make every row become same reference    
* "{}".format(5) -> "5"
    "{{}}{}".format(5) -> "{}5"
* **Post order** traversal: use stack, **right tree** append first, then **reverse** the result-> [#112](./112_PathSum.py), [#113](./113_PathSumII.py), [#145](./145_PostorderTraversal.py)
* DFS in stack -> one stack will be good (**Preorder**)
* BFS in stack -> 
    * have 2 stacks, curr and next
    * store next level nodes in next
    * go through all nodes in curr
    * swap curr and next, then clear next

* DFS如果只是traverse 可以用stack (因為會不知道斷點 不知道什麼時候走到底了), 如果是一層一層累積的可能就得用recursion
* Binary Search Tree: -> [#669](./669_TrimBinaryTree.py)
    * any node of *left* subtree must **<=** root val
    * any node of *right* subtree must **>** root val

* list.index(value) -> get index -> [#654](./654_MaximumBinaryTree.py)
* Traverse的時候如果終止條件之後直接先跑遞迴 可以變bottom-up
*  if there is a child, the depth should keep counting -> [#111](./111_MinDepthOfBinaryTree.py) 
 -> if not root.left return self.minDepth(root.right) + 1 
 -> if not root right return self.minDepth(root.left) + 1

## Problems

### Easy

* [No. 404 Sum of Left Leaves](./404_SumOfLeftLeaves.py) --- [Solution Video](https://www.youtube.com/watch?v=-79mkmH2lZs&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=49)
* [No. 637 Average of Levels in Binary Tree](./637_AvgLvlInBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=3VljCEnwcdU&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=46)
* [No. 617 Merge Two Binary Trees](./617_MergeTwoTrees.py) --- [Solution Video](https://www.youtube.com/watch?v=EmVsf2sMNiU&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=45)
* [No. 606 Construct String from Binary Tree](./606_ConstructStringFromTree.py) --- [Solution Video](https://www.youtube.com/watch?v=EggWOgUnt2M&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=44)
* [No. 100 Same Tree](./100_SameTree.py) --- [Solution Video](https://www.youtube.com/watch?v=EggWOgUnt2M&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=42)
* [No. 110 Balanced Binary Tree](./110_BalancedBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=EggWOgUnt2M&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=41)
* [No. 671 Second Minimum Node in a Binary Tree](./671_2ndMinNode.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=39)
* [No. 669 Trim a Binary Search Tree](./669_TrimBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=38)
* [No. 690 Employee Importance](./Graph/690_EmployeeImportance.py) --- In [Graph](../Graph)
* [No. 687 Longest Univalue Path](./687_LongestUnivaluePath.py) --- [Solution Video](https://www.youtube.com/watch?v=yX1hVhcHcH8&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=25)
* [No. 543 Diameter of Binary Tree](./543_DiameterOfBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=yX1hVhcHcH8&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=24)
* [No. 104 Maximum Depth of Binary Tree](./104_MaxDepthOfBinaryTree.py) --- No video, mentioned in [Algo SP12](https://www.youtube.com/watch?v=PbGl8_-bZxI&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=5)
* [No. 111 Minimum Depth of Binary Tree](./111_MinDepthOfBinaryTree.py) --- No video, mentioned in [Algo SP12](https://www.youtube.com/watch?v=PbGl8_-bZxI&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=5)
* [No. 112 Path Sum](./112_PathSum.py) --- No video, mentioned in [Algo SP12](https://www.youtube.com/watch?v=PbGl8_-bZxI&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=5)
* [No. 101 Symmetric Tree](./101_SymmetricTree.py) --- No video, mentioned in [Algo SP12](https://www.youtube.com/watch?v=PbGl8_-bZxI&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=5)

### Medium

* [No. 208 Implement Trie](./208_ImplementTrie.py) --- [Solution Video](https://www.youtube.com/watch?v=f48wGD-MuQw&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=29)
* [No. 655 Print Binary Tree](./655_PrintBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=ipIL1qVAazk&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=47)
* [No. 113 Path Sum II](./113_PathSumII.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=43)
* [No. 102 Binary Tree Level Order Traversal](./102_LevelOrderTraversal.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=40)
* [No. 654 Maximum Binary Tree](./654_MaximumBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=37)
* [No. 307 Range Sum Query - Mutable](./307_RangeSumQueryMutable.py) --- [Solution Video](https://www.youtube.com/watch?v=WbafSgetDDk&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=14)
* [No. 332 Reconstruct Itinerary](../Graph/332_ReconstructItinerary.py) --- In [Graph](../Graph)
* [No. 677 Map Sum Pairs](../Design_DataStructure/677_MapSumPairs.py) --- In [Design & Data Structure](../Design_DataStructure)
* [No. 684 Redundant Connection](./Graph/684_RedundantConnection.py) --- In [Graph](../Graph)
* [No. 863 All Nodes Distance K in Binary Tree](../Graph/863_AllNodesDistanceKInBinaryTree.py) --- In [Graph](../Graph)
* [No. 951 Flip Equivalent Binary Trees](./951_FlipEquivalentBinaryTrees.py) --- No video, mentioned in [Algo SP12](https://www.youtube.com/watch?v=PbGl8_-bZxI&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=5)

### Hard

* [No. 145 Binary Tree Postorder Traversal](./145_PostorderTraversal.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=36)
* [No. 295 Find Median from Data Stream](../Design_DataStructure/295_FindMedian.py) --- In [Design & Data Structure](../Design_DataStructure)
* [No. 460 LFU Cache](../Design_DataStructure/460_LFUcache.py) --- In [Design & Data Structure](../Design_DataStructure)
* [No. 297 Serialize and Deserialize Binary Tree](../Design_DataStructure/297_CodecBinaryTree.py) --- In [Design & Data Structure](../Design_DataStructure)
* [No. 218 The Skyline Problem](./Geometry/218_TheSkylineProblem.py) --- In [Geometry](../Geometry)
* [No. 685 Redundant Connection II](../Graph/685_RedundantConnectionII.py) --- In [Graph](./Graph)
* [No. 315](./315_) --- [Solution Video](https://www.youtube.com/watch?v=2SVLYsq5W8M&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=11)