"""Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.

Examples:

source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.
source = "no", target = "go"
words = ["to"]

output: -1
"""

# use BFS to find the minimum dist b/n source to target
#  
from collections import deque


def shortestWordEditPath(source, target, words):
	
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    wordset = set(words)
    
    queue = deque([(source, 0)])
    
    seen = set(source)
    
    
    while queue:
      
      word, lvl = queue.popleft()
      
          #print(word)
      if word ==target:
        return lvl
      
      for i in range(len(source)):
        
        
        for c in alphabet:
          
          word2 = list(word)
          
          word2[i] = c
          
          word2 = "".join(word2)
          if word2 in wordset and word2 not in seen:
            queue.append((word2, lvl+1))
            seen.add(word2)
            
    return -1 