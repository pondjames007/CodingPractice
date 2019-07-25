# Binary Search

## Concepts
* bisect is handy
* implement Binary Search:
```
    i, j = 0, len(array)
    mid = (i+j)/2
    if target >= array[mid]:
        i = mid+1
    else:
        j = mid
```
* implement Binary Search on Linked List:
```
    # find out the mid point first -> quick slow pointers
    quick = head
    slow = head

    while quick and quick.next:
        quick = quick.next.next
        slow = slow.next

        return slow
```
* 注意 l, r 要用哪個東西
* 判斷條件是要用什麼
* 用bisect來計算多少數字大於/小於標準
## Problems

### Easy

* [No. 744 Find Smallest Letter Greater Than Target](./744_FindNextSmallestLetter.py) --- [Solution Video](https://www.youtube.com/watch?v=seQnf-5hlBo&list=PLLuMmzMTgVK74vqU7Ukaf70a382dzF3Uo&index=11)
* [No. 278 First Bad Version](./278_FirstBadVersion.py) --- [Solution Video](https://www.youtube.com/watch?v=v57lNF2mb_s&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=12)

### Medium

* [No. 729 My Calendar I](./729_MyCalendarI.py) --- [Solution Video](https://www.youtube.com/watch?v=seQnf-5hlBo&list=PLLuMmzMTgVK74vqU7Ukaf70a382dzF3Uo&index=12)
* [No. 540 Single Element in a Sorted Array](./540_SingleElementInSortedArray.py) --- [Solution Video](https://www.youtube.com/watch?v=seQnf-5hlBo&list=PLLuMmzMTgVK74vqU7Ukaf70a382dzF3Uo&index=10)
* [NO. 792 Number of Matching Sequences](../String/792_NumberOfMatchingSubsequences.py) --- In [String](../String)
* [No. 875 Koko Eating Bananas](./875_KokoEatingBananas.py) --- [Solution Video](https://www.youtube.com/watch?v=v57lNF2mb_s&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=12)
* [No. 378 Kth Smallest Element in a Sorted Matrix](./378_KSmallestElementInSortedMatrix.py) --- [Solution Video](https://www.youtube.com/watch?v=v57lNF2mb_s&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=12)

### Hard

* [No. 719 Find K-th Smallest Pair Distance](./719_FindKthSmallestPairDistance.py) --- [Solution Video](https://www.youtube.com/watch?v=seQnf-5hlBo&list=PLLuMmzMTgVK74vqU7Ukaf70a382dzF3Uo&index=14)