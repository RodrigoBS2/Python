from collections import deque

# Create a deque
dq = deque([10, 20, 30, 40, 50, 20, 30, 20])

# 1. Counting occurrences of a value
print(dq.count(20))  # Occurrences of 20
print(dq.count(30))  # Occurrences of 30

# 2. Rotating the deque
dq.rotate(2)  # Rotate the deque 2 steps to the right
print(dq)

dq.rotate(-3)  # Rotate the deque 3 steps to the left
print(dq)

# 3. Reversing the deque
dq.reverse()  # Reverse the deque
print(dq)