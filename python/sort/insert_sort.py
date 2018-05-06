def insert_sort(lst):
  """ Insert sort a list
  :type arr: list
  :param arr: List to sort
  :returns: list -- Sorted list
  """
  for j in range(1, len(lst)):
    while j > 0 and lst[j-1] > lst[j]:
      lst[j], lst[j-1] = lst[j-1], lst[j]

      j -= 1

  return lst

print(insert_sort([1,8,-45,0,2]))