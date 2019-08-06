# Search

## Concepts
* stack
* DFS recursion
* [#547](./547_FriendCircles.py) -> [#200](./200_NumberOfIslands.py)
* import string: string.ascii_lowercase: -> it will give a string of a-z
* Combination C(len(nums), n) 組合不需要多一個數組 但是跑的時候要從現在的元素後面一個開始看 -> [#039](./039_CombinationSum.py), [#040](./040_CombinationSumII.py), [#216](./216_CombinationSumIII.py)
```
C(nums, n, d, s, curr, ans) # s == pick from which element
	if d == n:
		ans.append(curr)
		return
	for i = s to len(nums)
		curr.push(nums[i])
		C(nums, d+1, n, i+1, curr, ans)
		curr.pop()
```

* Permutation P(len(nums), n) 排列必須多一個數組來存用過的元素
```
P(nums, n, d, used, curr, ans): # list, pickNo., recursive depth, the list is used or not, current permutation list, answer
	if d == n:
		ans.append(curr)
		return

	for i = 0 to len(nums):
		if used[i]: continue
		used[i] = True
		curr.push(nums[i])
		P(nums, d+1, n, curr, ans)
		curr.pop()
		used[i] = False
```
* **pass in reference** only in **mutable objects**! immutable objects are not
* **Mutable Objects**: list, dict, set, byte array, class objects
* **Immutable Objects**: numbers, string, tuple, frozen set

## Problems

### Easy

* [No. 733 Flood Fill](../Graph/733_FloodFill.py) --- In [Graph](../Graph)

### Medium

* [No. 079 Word Search](./079_WordSearch.py) --- [Solution Video](https://www.youtube.com/watch?v=oUeGFKZvoo4&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=34)
* [No. 200 Number of Islands](./200_NumberOfIslands.py) --- [Solution Video](https://www.youtube.com/watch?v=XSmgFKe-XYU&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=31)
* [No. 547 Friend Circles](./547_FriendCircles.py) --- [Solution Video](https://www.youtube.com/watch?v=HHiHno66j40&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=30)
* [No. 127 Word Ladder](./127_WordLadder.py) --- [Solution Video](https://www.youtube.com/watch?v=vWPCm69MSfs&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=29)
* [No. 039 Combination Sum](./039_CombinationSum.py) --- [Solution Video](https://www.youtube.com/watch?v=zIY2BWdsbFs&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=27)
* [No. 040 Combinarion Sum II](./040_CombinationSumII.py) --- [Solution Video](https://www.youtube.com/watch?v=RSatA4uVBDQ&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=25)
* [No. 216 Combinarion Sum III](./216_CombinationSumIII.py) --- [Solution Video](https://www.youtube.com/watch?v=RSatA4uVBDQ&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=23)
* [No. 017 Letter Combinations of a Phone Number](./017_LetterCombOfPhoneNum.py) --- [Solution Video](https://www.youtube.com/watch?v=RSatA4uVBDQ&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=18)
* [No. 322 Coin Change](./322_CoinChange.py) --- [Solution Video](https://www.youtube.com/watch?v=RSatA4uVBDQ&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=17)
* [No. 787 Cheapest Flight within K Stops](./787_CheapestFlightKStops.py) --- [Solution Video](https://www.youtube.com/watch?v=RSatA4uVBDQ&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=13)
* [No. 801 Mimimum Swaps to Make Sequence Increasing](./801_MinimumSwapsToSeq.py) --- [Solution Video](https://www.youtube.com/watch?v=RSatA4uVBDQ&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=9)
* [No. 078 Subset](../Bit/078_Subsets.py) --- In [Bit](../Bit)
* [No. 967 Numbers with Same Consecutive Differences](./967_NumbersWithSameConsecutiveDiff.py) --- [Solution Video](https://www.youtube.com/watch?v=qFLE3KY7vRU&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=3)
* [No. 417 Pacific Atlantic Water Flow](./417_PacificAtlanticWaterFlow.py) --- [Solution Video](https://www.youtube.com/watch?v=qFLE3KY7vRU&list=PLLuMmzMTgVK423Mj1n_OaOAZZ6k5fNxyN&index=1)

### Hard
