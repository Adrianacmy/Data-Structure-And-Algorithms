# sort an array to increase
# runtime O(n2), it is only usefull for small dataset
def select_sort(arr):
  for i in range(len(arr)):
    minIdx = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[minIdx]:
        minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

  return arr

print(select_sort([1,5,7,45,0,12,-8]))