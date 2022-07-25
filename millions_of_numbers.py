# time used 60 - 37 = 23 mins
# thought process: use hash/dictionary
# add any key with val (count) of 3 to results array
# sort results (if required) and return the array

def millions_of_numbers(ary1, ary2, ary3):
  nums = ary1 + ary2 + ary3
  my_dict = {}
  results = []
  for num in nums:
    if my_dict.__contains__(num):
      my_dict[num] += 1
      if my_dict[num] == 3:
        results.append(num)
    else:
      my_dict[num] = 1
  results.sort()
  return results

nums_1 = [1, 2, 4, 5, 8]
nums_2 = [2, 3, 5, 7, 9]
nums_3 = [1, 2, 5, 8, 9]
print(millions_of_numbers(nums_1, nums_2, nums_3))
