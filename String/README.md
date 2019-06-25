# String

## Concepts
* zip() -> [#848](./848_ShiftingLetters.py)
* bisect: do binary search on a **sorted** list -> [#792](./792_NumberOfMatchingSubsequences.py)
```
    import bisect


    bisect.bisect_left(L,x) # 3
    # 在L中查找x，x存在時返回x最左側的位置，x不存在返回應該插入的位置

    bisect.bisect_right(L,x) # 6
    # 在L中查找x，x存在時返回x最右側的位置，x不存在返回應該插入的位置

    bisect.insort_left(L,x) # [1, 3, 4, 5, 5, 5, 5, 8, 10]
    # 將x插入到列表L中，x存在時插入在左側

    bisect.insort_right(L,x) # [1, 3, 4, 5, 5, 5, 5, 5, 8, 10]
    # 將x插入到列表L中，x存在時插入在右側
```
* isalpha(): check if a char is a letter -> [#784](./784_LetterCasePermutation.py)
* all(): return True if all elements in a list are all True -> [#748](./748_ShortestCompletingWord.py) 
* [Trie](https://zh.wikipedia.org/wiki/Trie) -> [#720](./720_LongestWordInDictionary.py)
    用空間換時間
    多層的hash table
    每一層每一級key的長度都是1
    在每個節點標記是不是在字典裡
    應用不多 特殊場合很高效
    [#208](../BinaryTree/208_ImplementTrie.py) shows how to implement Trie

## Problems

### Easy

* [No. 784 Letter Case Permutation](./784_LetterCasePermutation.py) --- [Solution Video](https://www.youtube.com/watch?v=LJifc-ehvBM&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=3)
* [No. 748 Shortest Completing Word](./748_ShortestCompletingWord.py) --- [Solution Video](https://www.youtube.com/watch?v=vHzPkqpPiWk&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=8)
* [No. 720 Longest Word in Dictionary](./720_LongestWordInDictionary.py) --- [Solution Video](https://www.youtube.com/watch?v=TqrZg4wYP1U&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=12)

### Medium

* [No. 848 Shifting Letters](./848_ShiftingLetters.py) --- [Solution Video](https://www.youtube.com/watch?v=gOycoA8pOqg&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz)
* [NO. 792 Number of Matching Sequences](./792_NumberOfMatchingSubsequences.py) --- [Solution Video](https://www.youtube.com/watch?v=l8_vcmjQA4g&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=2)
* [No. 763 Partition Labels](./763_PartitionLabels.py) --- [Solution Video](https://www.youtube.com/watch?v=s-1W5FDJ0lw&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=5)
