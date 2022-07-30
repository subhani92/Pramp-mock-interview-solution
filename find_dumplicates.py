"""Find The Duplicates
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2 """

#time complexity O(m+n) solution two pointer 
def find_duplicates(arr1, arr2):
  
  l1, l2= len(arr1), len(arr2)
  
  pointer_1, pointer_2 = 0, 0 
  
  output = []
  
  while pointer_1 < l1 and pointer_2 <l2:
    
    if arr1[pointer_1] == arr2[pointer_2]:
      output.append(arr1[pointer_1])
      pointer_1 +=1
      pointer_2 +=1
      
    elif arr1[pointer_1] < arr2[pointer_2]:
       pointer_1 +=1
        
    else:
       pointer_2 +=1
      
  return output 



## solution 2 binary search (nlogm) solution 
def find_duplicates(arr1, arr2):
  
  l1, l2= len(arr1), len(arr2)
  
  
  output = []
  
  for i in range(l1):
    
    exist = binary_search(arr2, arr1[i])
    
    if exist != -1:
      output.append(exist)

  
  return output 
     

def binary_search(arr, target):
  
  l, r = 0, len(arr)-1
  
  while l<=r:
    
    mid = l +(r-l)//2
    
    if arr[mid] == target:
      return arr[mid]
    elif arr[mid] < target:
      l = mid+1
    else:
      r =  mid-1 
    
  return -1 
