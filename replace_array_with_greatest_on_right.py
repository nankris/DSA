def replaceElements(arr):
    for i in range(len(arr)-1, -1, -1):
        if i == len(arr)-1:
            max_till_now = arr[i]
            arr[i] = -1
        else:
            if arr[i] > max_till_now:
                print(i, max_till_now)
                tmp = arr[i]
                arr[i] = max_till_now
                max_till_now = tmp
            else:
                arr[i] = max_till_now
    return arr



arr = [17,18,5,4,6,1]
print(replaceElements(arr))
