# String

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
* Post order traversal: use stack -> [#113](./113_PathSumII.py)

## Problems

### Easy

* [No. 404 Sum of Left Leaves](./404_SumOfLeftLeaves.py) --- [Solution Video](https://www.youtube.com/watch?v=-79mkmH2lZs&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=49)
* [No. 637 Average of Levels in Binary Tree](./637_AvgLvlInBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=3VljCEnwcdU&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=46)
* [No. 617 Merge Two Binary Trees](./617_MergeTwoTrees.py) --- [Solution Video](https://www.youtube.com/watch?v=EmVsf2sMNiU&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=45)
* [No. 606 Construct String from Binary Tree](./606_ConstructStringFromTree.py) --- [Solution Video](https://www.youtube.com/watch?v=EggWOgUnt2M&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=44)

### Medium

* [No. 208 Implement Trie](./208_ImplementTrie.py) --- [Solution Video](https://www.youtube.com/watch?v=f48wGD-MuQw&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=29)
* [No. 655 Print Binary Tree](./655_PrintBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=ipIL1qVAazk&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=47)
* [No. 113 Path Sum II](./113_PathSumII.py) --- [Solution Video](https://www.youtube.com/watch?v=zrN2dxtQ0f0&list=PLLuMmzMTgVK7ug02DDoQsf50OtwVDL1xd&index=43)