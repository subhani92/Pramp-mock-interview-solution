""""
Getting a Different Number
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4 

""""

#O(n) solution 

def get_different_number(arr):
  
  
  for i in range(len(arr)):
    
    # if number is leas than array size mark it by multiplying -1 
    temp = abs(arr[i])
    #print(temp)
    if temp < len(arr):
      
      arr[temp] = -1*arr[temp]
      
  print(arr)
  for i in range(len(arr)):
    
    # if number is positive return index
    if arr[i] >0 and arr[i]:
      return i
  
  return len(arr)
      
  
print(get_different_number([0,1,2,2]))
  
print(get_different_number([1000,2,3]))


