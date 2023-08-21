from collections import Counter

counter1 = Counter("abbccc")
counter2 = Counter("cbacbc")

print(counter1 == counter2)  # Output: True

# Example 2
counter3 = Counter([1, 2, 2, 3, 3, 3, 4])
counter4 = Counter([3, 3, 2, 2, 1, 4, 3])

print(counter3, counter4)

counter3[5] = 0

print(counter3, counter4)

print(counter3 == counter4)  # Output: True
