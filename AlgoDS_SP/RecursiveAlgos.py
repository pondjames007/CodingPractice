# GROUP 1
## Quick Sort
def quick_sort(a, l, r): # a = unsorted list, l = left bound, r = right bound
    # a will be directly sorted
    def partition(a, l, r):
        return random.randint(l, r)
        
    p = partition(a, l, r)
    quick_sort(a, l, p)
    quick_sort(a, p+1, r)

## Merge Sort
def merge_sort(a, l, r):
    m = (l + r)/2
    merge_sort(a, l, m)
    merge_sort(a, m+1, r)
    merge(a, l, m, r) 


# GROUP 2
## Binary Search
def binary_search(a, l, r):
    m = (l + r)/2
    if f(m): binary_search(a, l, m)
    else: binary_search(a, m+1, r)

## Inorder Traversal
def inorder(root):
    inorder(root.left)
    func(root.val)
    inorder(root.right)


# GROUP 3
## Combination Pseudo
def combination(d, s): # depth, start
    if d == n: return func()
    for i in range(s, n):
        combination(d+1, i+1)

## Combination real: C(len(nums), n)
def Combination(nums, n, d, s, curr, ans): # list, no. to pick, recursive depth, start element, current combination list, answer
    if d == n:
        ans.append(curr)
        return
    
    for i in range(s, len(nums)):
        curr.push(nums[i])
        Combination(nums, d+1, n, i+1, curr, ans)
        curr.pop()

    return

## Permutation Pseudo
def permutation(d, used):
    if d == n: return func()
    for i in range(0, n):
        if i in used: continue
        used.add(i)
        permutation(d+1, used)
        used.remove(i)

## Permutation real: P(len(nums), n)
def Permutation(nums, n, d, used, curr, ans): # list, no. to pick, recursive depth, a list to record used or not, current combination list, answer
    if d == n:
        ans.append(curr)
        return

    for i in range(len(nums)):
        if used[i]: continue
        used[i] = True
        curr.push(nums[i])
        Permutation(nums, n, d+1, used, curr, ans)
        curr.pop()
        used[i] = False

    return