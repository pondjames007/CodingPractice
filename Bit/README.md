# Bit

## Concepts
* [Boyer-Moore Vote Algorithm](https://zh.wikipedia.org/wiki/Boyer-Moore%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95) -> [#169](./169_MajorityElement.py)
* Bit Vote:
Bit Vote (it seems that Python is not good at handling bit manipulation in negative number) -> [#169](./169_MajorityElement.py)
C++ version is good
將數字視為32bit
走過每個位元 看過每個數字 如果在第i位出現0的機率(次數)>1的機率(次數) -> 第i位是0, 反之
由於majority > n/2 所以會主導每一個位元出現0或是1
* map(func, iter): return a list by applying every element in iter to func -> [#477](./477_TotalHammingDistance.py)
    JS: Array.map(func)
* zip(a, b) -> 返回一個obj, 可以list化, 返回的list會是[(a[0], b[0]), (a[1], b[1]), ...] -> [#477](./477_TotalHammingDistance.py)
* zip(*li) -> 將list裡的iterable(string, list, tuple, ...) "解壓" 回原本的 (逆操作) -> [#477](./477_TotalHammingDistance.py)
* '{:032b}'.format(num): return binary version of num in **32** bits
* int(bin, 2): return the decimal version number from bin string
* bin(num): return binary string with least requirement bits, and with prefix '0b' for positive and '-0b' for negative
* ~n: '~' takes compliment -> return -n-1
* prime number: go through 2 to n/2, or sqrt(n), and check if it can be divided -> [#762](./762_PrimeNumSetBits.py)
## Problems

### Easy

* [No. 169 Majority Element](./169_MajorityElement.py) --- [Solution Video](https://www.youtube.com/watch?v=LPIvL-jvGdA&list=PLLuMmzMTgVK7t8spH-USywHZLtt2aM5Ue&index=8)
* [No. 476 Number Complement](./476_NumberComplement.py) --- [Solution Video](https://www.youtube.com/watch?v=LPIvL-jvGdA&list=PLLuMmzMTgVK7t8spH-USywHZLtt2aM5Ue&index=6)
* [No. 762 Prime Number of Set Bits in Binary Representation](./762_PrimeNumSetBits.py) --- [Solution Video](https://www.youtube.com/watch?v=LPIvL-jvGdA&list=PLLuMmzMTgVK7t8spH-USywHZLtt2aM5Ue&index=5)

### Medium

* [No. 477 Total Hamming Distance](./477_TotalHammingDistance.py) --- [Solution Video](https://www.youtube.com/watch?v=LPIvL-jvGdA&list=PLLuMmzMTgVK7t8spH-USywHZLtt2aM5Ue&index=7)
* [No. 289 Game of Life](./289_GameOfLife.py) --- [Solution Video](https://www.youtube.com/watch?v=LPIvL-jvGdA&list=PLLuMmzMTgVK7t8spH-USywHZLtt2aM5Ue&index=4)