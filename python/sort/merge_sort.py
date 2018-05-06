# 

def merge_sort(x):
  '''
  Insert sort a list
  
  runtime: nlogn
  fastest sort for comparizon based sort algorithm
  effient for large dataset  
 
  :type x: list
  :param x: List to sort
  :returns: list -- Sorted list
  '''
  if len(x) < 2:return x

  result,mid = [],int(len(x)/2)

  y = merge_sort(x[:mid])
  z = merge_sort(x[mid:])

  while (len(y) > 0) and (len(z) > 0):
          if y[0] > z[0]:result.append(z.pop(0))   
          else:result.append(y.pop(0))


  result.extend(y+z)
  return result


print(merge_sort([1,5,4,-45,9,20]))