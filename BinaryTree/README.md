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
* **Post order** traversal: use stack, **right tree** append first, then **reverse** the result-> [#113](./113_PathSumII.py), [#145](./145_PostorderTraversal.py)
    [#112] -> Path Sum I
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

## Problems

### Easy

* [No. 404 Sum of Left Leaves](./404_SumOfLeftLeaves.py) --- [Solution Video](https://www.youtube.com/watch?v=-79mkmH2lZs&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=49)
* [No. 637 Average of Levels in Binary Tree](./637_AvgLvlInBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=3VljCEnwcdU&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=46)
* [No. 617 Merge Two Binary Trees](./617_MergeTwoTrees.py) --- [Solution Video](https://www.youtube.com/watch?v=EmVsf2sMNiU&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=45)
* [No. 606 Construct String from Binary Tree](./606_ConstructStringFromTree.py) --- [Solution Video](https://www.youtube.com/watch?v=EggWOgUnt2M&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=44)
* [No. 100 Same Tree](./100_SameTree.py) --- [Solution Video](https://www.youtube.com/watch?v=EggWOgUnt2M&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=42)
* [No. 110 Balanced Binary Tree](./110_BalancedBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=EggWOgUnt2M&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=41)
* [No. 671 Second Minimum Node in a Binary Tree](./671_2ndMinNode.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=39)
* [No. 669 Trim a Binary Search Tree](./BinaryTree/669_TrimBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=38)

### Medium

* [No. 208 Implement Trie](./208_ImplementTrie.py) --- [Solution Video](https://www.youtube.com/watch?v=f48wGD-MuQw&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=29)
* [No. 655 Print Binary Tree](./655_PrintBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=ipIL1qVAazk&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=47)
* [No. 113 Path Sum II](./113_PathSumII.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=43)
* [No. 102 Binary Tree Level Order Traversal](./102_LevelOrderTraversal.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=40)
* [No. 654 Maximum Binary Tree](./654_MaximumBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=37)

### Hard

* [No. 145 Binary Tree Postorder Traversal](./145_PostorderTraversal.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=36)