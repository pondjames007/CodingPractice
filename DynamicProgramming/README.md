# Dynamic Programming

## Concepts
* DP: remember the answer of sub questions -> TOP-DOWN or DOWN-TOP
* 計劃遞迴: 超過1000不建議使用
* 如果dp的狀況不是dense的 可以用hash table來代替array建立 省空間省時間
* [#494](./494_TargetSum.py) Optimization
    * Simpler Question: Subset Sum
        ```
            A = number array with length n
            Let P denotes a set of nums that have a '+' sign in front of it
            Let N denotes a set of nums that have a '-' sign in front of it

            Restriction for P and N:
            P U N = {A1, A2, ..., An} and P ∩ N = {Φ}

            Goal:
            Find out if there is a set P and N that
            sum(P) - sum(N) = target
            -> sum(P) + sum(P) = target + sum(P) + sum(N)
            -> sum(P) = (target + sum(A)) / 2
            -> 0/1 Knapsack Problem
        ```
        => We use Vi to denote the possible sums by using **any subset of** the first i elements
        => V0 = {0}
        => Vi = {Vi-1} U {Vi-1 + Ai} # Vi contains Vi-1, do we need to copy?
        => ans: check target in Vn
        => dp[i][j] := whether we can use the first i elements to sum up to j (j is in Vi)
        => init: dp[0][0] = True

## Problems

### Easy

* [No. 303 Range Sum Query - Immutable](./303_RangeSumQuery.py) --- [Solution Video](https://www.youtube.com/watch?v=pt-xIS6huIg&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=78)
* [No. 070 Climbing Stairs](./070_ClimbingStairs.py) --- [Solution Video](https://www.youtube.com/watch?v=pt-xIS6huIg&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=76)
* [No. 053 Maximum Subarray](./053_MaximumSubarray.py) --- [Solution Video](https://www.youtube.com/watch?v=pt-xIS6huIg&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=74)
* [No. 198 House Robber](./198_HouseRobber.py) --- [Solution Video](https://www.youtube.com/watch?v=H75Qp7ExCwo&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=52)
* [No. 746 Min Cost Climbing Stairs](./746_MinCostClimbingStairs.py) --- [Solution Video](https://www.youtube.com/watch?v=H75Qp7ExCwo&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=49)

### Medium

* [No. 120 Triangle](./120_Triangle.py) --- [Solution Video](https://www.youtube.com/watch?v=pt-xIS6huIg&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=75)
* [No. 139 Word Break](../HashTable/139_WordBreak.py) --- In [Hash Table](../HashTable)
* [No. 062 Unique Paths](./062_UniquePaths.py) --- [Solution Video](https://www.youtube.com/watch?v=fmpP5Ll0Azc&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=69)
* [No. 741 Cherry Pickup](./741_CherryPickup.py) --- [Solution Video](https://www.youtube.com/watch?v=fmpP5Ll0Azc&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=52)
* [No. 901 Online Stock Span](./901_OnlineStockSpan.py) --- [Solution Video](https://www.youtube.com/watch?v=RGRC46zHB98&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=19)
* [No. 926 Flip String to Monotone Increasing](./926_FlipString2MonotoneIncreasing.py) --- [Solution Video](https://www.youtube.com/watch?v=D8xa8ZMV7AI&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=18)
* [No. 801 Mimimum Swaps to Make Sequence Increasing](../Search/801_MinimumSwapsToSeq.py) --- In [Search](../Search)
* [No. 790 Domino and Tromino Tiling](./790_DominoTrominoTiling.py) --- [Solution Video](https://www.youtube.com/watch?v=S-fUTfqrdq8&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=41)
* [No. 712 Minimum ASCII Delete Sum for Two Strings](./712_MinASCIIDeleteSumFor2String.py) --- [Solution Video](https://www.youtube.com/watch?v=H75Qp7ExCwo&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=27)
* [No. 673 Number of Longest Increasing Subsequence](./673_NumLongestIncreasingSubsequence.py) --- [Solution Video](https://www.youtube.com/watch?v=fmpP5Ll0Azc&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=67)
* [No. 322 Coin Change](../Search/322_CoinChange.py) --- In [Search](../Search)
* [No. 494 Target Sum](./494_TargetSum.py) --- [Solution Video](https://www.youtube.com/watch?v=fmpP5Ll0Azc&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=44)
* [No. 813 Largest Sum of Averages](./813_LargestSumOfAvgs.py) --- [Solution Video](https://www.youtube.com/watch?v=fmpP5Ll0Azc&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=39)
* [No. 063 Unique Paths II](./063_UniquePathsII.py) --- [Solution Video](https://www.youtube.com/watch?v=IPdShoUE9z8&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=70)
* [No. 064 Minimum Path Sum](./064_MinPathSum.py) --- [Solution Video](https://www.youtube.com/watch?v=IPdShoUE9z8&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=54)
* [No. 688 Knight Probability in Chessboard](./688_KnightProbabilityInChessboard.py) --- [Solution Video](https://www.youtube.com/watch?v=IPdShoUE9z8&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=62)
* [No. 576 Out of Boundary Paths](./576_OutOfBoundaryPaths.py) --- [Solution Video](https://www.youtube.com/watch?v=IPdShoUE9z8&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=31)

### Hard

* [No. 072 Edit Distance](./072_EditDistance.py) --- [Solution Video](https://www.youtube.com/watch?v=H75Qp7ExCwo&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=61)
* [No. 312 Burst Balloons](./312_BurstBalloons.py) --- [Solution Video](https://www.youtube.com/watch?v=fmpP5Ll0Azc&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr&index=78)