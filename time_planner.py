"""
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose dur
"""

def meeting_planner(slotsA, slotsB, dur):
  
  
  pointer_a, pointer_b = 0 , 0
  
  len_a , len_b  = len(slotsA), len(slotsB)
  
  while pointer_a < len_a and pointer_b < len_b:
    
    start_a, end_a = slotsA[pointer_a]
    start_b, end_b = slotsB[pointer_b]
    
    
    t1 = max(start_a, start_b)
    t2 = min(end_a, end_b)
    
    
    #print(t1, t2 )
    
    if abs(t1-t2) >= dur:
      return [t1, t1+dur]
    
    else:
      if end_a > end_b:
        pointer_b +=1
        
      elif end_a < end_b:
        pointer_a +=1
        
        
  return []
  
  
  
#slotsA = [[10, 50], [60, 120], [140, 210]]
#slotsB = [[0, 15], [60, 70]]
#print( meeting_planner(slotsA, slotsB, dur ))
  
#Otime O(N+M) space O(1)


