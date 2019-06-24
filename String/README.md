# String

## Concepts
* zip() -> [#848](./String/848_ShiftingLetters.py)
* bisect: do binary search on a **sorted** list -> [#792](./String/792_NumberOfMatchingSubsequences.py)
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
* isalpha(): check if a char is a letter -> [#784](./String/784_LetterCasePermutation.py)
* all(): return True if all elements in a list are all True -> [#748](./String/748_ShortestCompletingWord.py) 
* [Trie](https://zh.wikipedia.org/wiki/Trie) -> [#720](./String/720_LongestWordInDictionary.py)
## Problems
* [No. 784 Letter Case Permutation](./String/784_LetterCasePermutation.py) **Easy** [Solution Video](https://www.youtube.com/watch?v=LJifc-ehvBM&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=3)
* [No. 748 Shortest Completing Word](./String/748_ShortestCompletingWord.py) **Easy** [Solution Video](https://www.youtube.com/watch?v=vHzPkqpPiWk&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=8)
* [No. 720 Longest Word in Dictionary](./String/720_LongestWordInDictionary.py) **Easy** [Solution Video](https://www.youtube.com/watch?v=TqrZg4wYP1U&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=12)
* [No. 848 Shifting Letters](./String/848_ShiftingLetters.py) **Medium**: [Solution Video](https://www.youtube.com/watch?v=gOycoA8pOqg&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz)
* [NO. 792 Number of Matching Sequences](./String/792_NumberOfMatchingSubsequences.py) **Medium** [Solution Video](https://www.youtube.com/watch?v=l8_vcmjQA4g&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=2)
* [No. 763 Partition Labels](./String/763_PartitionLabels.py) **Medium** [Solution Video](https://www.youtube.com/watch?v=s-1W5FDJ0lw&list=PLLuMmzMTgVK49Hph4vV8DAzGZpj4azwmz&index=5)
