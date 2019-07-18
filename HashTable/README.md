# Hash Table

## Concepts
* queue.PriorityQueue vs heapq -> heapq is faster and more flexible. PQ is safer but only does queue functionality
* collections.OrderedDict -> [#146](./146_LRUcache.py)
* [#146](./146_LRUcache.py)</br>
    Access to a random key in O(1) -> hash table</br>
    Remove the last entry in LRU cache in O(1) -> linkedlist, vector</br>
    Add/Move an entry to the front of LRU cache in O(1) -> linkedlist</br>
        -> **bidirection Linkedlist**</br>
* Sort a list (defaut **ASCENDING ORDER**)-> [#451](./451_SortCharByFreq.py)</br>
    sorted(list, key= func, reverse= False)</br>
    list.sort(key= , reverse= ) </br>
* 快慢指針 -> [#141](./141_LinkedListCycle.py)</br>
    快指針每次移動兩個(以上)的指針</br>
    慢指針每次移動一個</br>
    如果慢指針碰到快指針 代表有環</br>
* 動態規劃 -> [#139](./139_WordBreak.py)</br>
    特性: 可以分解成子問題</br>
    前 i 個字符可以被分割的話 剩下的子串也是在字典裡 就是有解</br>
    要找break節點 若找到一個節點分開兩邊均有解的話就是有解</br>
    動態規劃的精神就是比較小規模的資料是否有解</br>
    動態規劃本質就是計劃遞歸</br>
    遞歸求解把解記住 若是下次遇到同樣的子問題可以直接從記憶體拿出來不用再算一次</br>
* Fuzzy Match/Search -> [#676](./676_MagicDictionary.py)</br>
	在建立的時候把每個字元變星號與改掉的原字元存下來
    
```
	input list: ['hello']
	dict = {'*ello': 'h', 'h*ello': 'e', ......}
```
</br>
	搜尋的時候就是把每個字元都變星號 並且不能是原本的字元

* heapq: 都是直接call 對象要放在function裡面當argument
* 底線functions
* 知道資料範圍的時候其實可以用list來儲存 (e.g. 英文字母就26個)
## Problems

### Easy

* [No. 001 Two Sum](./001_TwoSum.py) --- [Solution Video](https://www.youtube.com/watch?v=tNtk_rwbaIk&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=30)
* [No. 141 Linked List Cycle](./141_LinkedListCycle.py) --- [Solution Video](https://www.youtube.com/watch?v=bxCb37nLXWM&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=29)
* [No. 409 Longest Palindrome](../String/409_LongestPalindrome.py) --- In [String](../String)
* [No. 169 Majority Element](../Bit/169_MajorityElement.py) --- In [Bit](../Bit)
* [No. 720 Longest Word in Dictionary](../String/720_LongestWordInDictionary.py) --- In [String](../String)
* [No. 748 Shortest Completing Word](../String/748_ShortestCompletingWord.py) --- In [String](../String)
* [No. 438 Find All Anagrams in a String](./438_FindAllAnagramsInString.py) --- [Solution Video](https://www.youtube.com/watch?v=bxCb37nLXWM&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=7)
### Medium

* [No. 139 Word Break](./139_WordBreak.py) --- [Solution Video](https://www.youtube.com/watch?v=bxCb37nLXWM&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=28), [New Version](https://www.youtube.com/watch?v=ptlwluzeC1I&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop)
* [No. 676 Implement Magical Dictionary](./676_MagicDictionary.py) --- [Solution Video](https://www.youtube.com/watch?v=wq9XjoKMxek&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=27)
* [No. 146 LRU Cache](./146_LRUcache.py) --- [Solution Video](https://www.youtube.com/watch?v=q1Njd3NWvlY&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=26)
* [No. 451 Sort Characters By Frequency](./451_SortCharByFreq.py) --- [Solution Video](https://www.youtube.com/watch?v=qdpBD0LFgN0&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=25)
* [No. 380 Insert Delete GetRandom O(1)](../Design_DataStructure/380_InsDelGetRdm.py) --- In [Design & Data Structure](../Design_DataStructure)
* [No. 677 Map Sum Pairs](../Design_DataStructure/677_MapSumPairs.py) --- In [Design & Data Structure](../Design_DataStructure)
* [No. 692 Top K Frequent Words](./692_TopKFreqWords.py) --- [Solution Video](https://www.youtube.com/watch?v=POERw4yDVBw&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=19)
* [No. 347 Top K Frequent Elements](./347_TopKFreqElements.py) --- [Solution Video](https://www.youtube.com/watch?v=POERw4yDVBw&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=18)
* [No. 763 Partition Labels](../String/763_PartitionLabels.py) --- In [String](../String)
* [No. 792 Number of Matching Subsequences](../String/792_NumberOfMatchingSubsequences.py) --- In [String](../String)
* [No. 560 Subarray Sum Equals K](./560_SubarraySumEqualsK.py) --- [Solution Video](https://www.youtube.com/watch?v=POERw4yDVBw&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=9)
* [No. 567 Permutation in String](./567_PermutationInString.py) --- [Solution Video](https://www.youtube.com/watch?v=bxCb37nLXWM&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=6)
* [No. 525 Contiguous Array](./525_ContiguousArray.py) --- [Solution Video](https://www.youtube.com/watch?v=bxCb37nLXWM&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=5)

### Hard

* [No. 381 Insert Delete GetRandom O(1) - Duplicates allowed](../Design_DataStructure/381_InsDelGetRdm_Dup.py) --- In [Design & Data Structure](../Design_DataStructure)
* [No. 432 All O(1) Data Structure](../Design_DataStructure/432_AllOneDS.py) --- In [Design & Data Structure](../Design_DataStructure)