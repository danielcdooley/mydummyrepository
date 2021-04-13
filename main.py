
# Problem from LeetCode: https://leetcode.com/problems/shuffle-string/  

# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

# Input: s = "art", indices = [1,0,2]
# Output: "rat"

def shuffle_string(s, array_indices):
  n = len(s)
  t = [None] * n

  for i, ch in enumerate(s):
    output_index = array_indices[i]
    t[output_index] = ch
  return ''.join(t)

shuffled_string = shuffle_string('art', [1, 0, 2])
print(shuffled_string)



