# Design and Data Structure

## Concepts
* use 2 heaps to find median (1 'Min' -> get median+1 element and 1 'Max' -> get median-1 element) -> [#295](./295_FindMedian.py)
* use array + dict to have fast Set insertion/removal/random
* don't use **del** to delete element in the dictionary (slow), use **pop** instead -> [#380](./380_InsDelGetRdm.py)
* collections.defaultdict: can assign the dict with default value type -> [#381](./381_InsDelGetRdm_Dup.py)
* if 'something': will return false if the length == 0
* find the rest with prefix: use stack BFS and check the type to prevent termination node be counted as character node -> [#677](./677_MapSumPairs.py)
## Problems

### Easy

* 
### Medium

* [No. 676 Implement Magic Dictionary](../HashTable/676_MagicDictionary.py) --- In [Hash Table](../HashTable)
* [No. 146 LRU Cache](../HashTable/146_LRUcache.py) --- In [Hash Table](../HashTable)
* [No. 380 Insert Delete GetRandom O(1)](./380_InsDelGetRdm.py) --- [Solution Video](https://www.youtube.com/watch?v=y240Qh9H9uk&list=PLLuMmzMTgVK6M8XmintFnrd1VN-VBc0t0&index=10)
* [No. 677 Map Sum Paris](./677_MapSumPairs.py) --- [Solution Video](https://www.youtube.com/watch?v=y240Qh9H9uk&list=PLLuMmzMTgVK6M8XmintFnrd1VN-VBc0t0&index=7)

### Hard

* [No. 295 Find Median from Data Stream](./295_FindMedian.py) --- [Solution Video](https://www.youtube.com/watch?v=60xnYZ21Ir0&list=PLLuMmzMTgVK6M8XmintFnrd1VN-VBc0t0&index=12)
* [No. 381 Insert Delete GetRandom O(1) with Duplicates Allowed](./381_InsDelGetRdm_Dup.py) --- [Solution Video](https://www.youtube.com/watch?v=y240Qh9H9uk&list=PLLuMmzMTgVK6M8XmintFnrd1VN-VBc0t0&index=9)
* [No. 297 Serialize and Deserialize Binary Tree](./297_CodecBinaryTree.py) --- [Solution Video](https://www.youtube.com/watch?v=y240Qh9H9uk&list=PLLuMmzMTgVK6M8XmintFnrd1VN-VBc0t0&index=8)
* [No. 432 All O(1) Data Structure](./432_AllOneDS.py) --- [Solution Video](https://www.youtube.com/watch?v=wYqLisoH80w&list=PLLuMmzMTgVK6M8XmintFnrd1VN-VBc0t0&index=3)