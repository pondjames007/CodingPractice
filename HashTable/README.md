# Hash Table

## Concepts
* queue.PriorityQueue vs heapq -> heapq is faster and more flexible. PQ is safer but only does queue functionality
* collections.OrderedDict -> [#146](./146_LRUcache.py)
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
    搜尋的時候就是把每個字元都變星號 並且不能是原本的字元

* [#126](./146_LRUcache.py)</br>
    Access to a random key in O(1) -> hash table</br>
    Remove the last entry in LRU cache in O(1) -> linkedlist, vector</br>
    Add/Move an entry to the front of LRU cache in O(1) -> linkedlist</br>
        -> **bidirection Linkedlist**</br>
        
## Problems

### Easy

* [No. 001 Two Sum](./001_TwoSum.py) --- [Solution Video](https://www.youtube.com/watch?v=tNtk_rwbaIk&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=30)
* [No. 141 Linked List Cycle](./141_LinkedListCycle.py) --- [Solution Video](https://www.youtube.com/watch?v=bxCb37nLXWM&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=29)

### Medium

* [No. 139 Word Break](./139_WordBreak.py) --- [Solution Video](https://www.youtube.com/watch?v=bxCb37nLXWM&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=28), [New Version](https://www.youtube.com/watch?v=ptlwluzeC1I&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop)
* [No. 676 Implement Magical Dictionary](./676_MagicDictionary.py) --- [Solution Video](https://www.youtube.com/watch?v=wq9XjoKMxek&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=27)
* [No. 146 LRU Cache](./146_LRUcache.py) --- [Solution Video](https://www.youtube.com/watch?v=q1Njd3NWvlY&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=26)
* [No. 451 Sort Characters By Frequency](./451_SortCharByFreq.py) --- [Solution Video](https://www.youtube.com/watch?v=qdpBD0LFgN0&list=PLLuMmzMTgVK48qe6jxrVW-FHNrm7g5mop&index=25)