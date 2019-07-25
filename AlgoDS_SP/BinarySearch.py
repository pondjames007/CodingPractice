def binary_search(l, r):
    while l < r:
        m = (l+r)/2
        if f(m): return m # check if m is the answer or not (optional)
        if g(m): # check next round should go left or right
            r = m   # new range [l,m)
        else:
            l = m+1 # new range [m+1, r)

    return l # or not found