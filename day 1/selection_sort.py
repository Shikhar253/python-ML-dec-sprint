def selection_sort(arr):
    for i in range (0,len(arr)-1):
        min_val=arr[i]
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_idx=j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return(arr)

if __name__=="__main__":
    print(selection_sort([4,2,5,6,1,1,3]))
    