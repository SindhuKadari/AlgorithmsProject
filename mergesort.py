def mergesort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = mergesort(a[:mid])
        right = mergesort(a[mid:])
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a
a=[1,3,5,7,0,-1]
print(mergesort(a))
