def bubble_sort(arr):
    for j in range(len(arr)-1):
        swapped = False   # track if any swap happened in this pass
        
        # 1st mein largest last, 2nd mein 2nd largest last ...
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        # If no swap → array sorted → break early  (isse best case O(n) ho jaata hai)
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    print(bubble_sort([4, 2, 5, 6, 1, 1, 3]))
