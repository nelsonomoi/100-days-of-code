# A set is an unordered collections of items
# every element is unique

# syntax
set_name = {1,2,3,4,5}

# creating empty set
set_name = ()

# in a set every element is unique
set_2 = {1,2,3,3,4,5}
print(set_2)

# Union
# set of all elements in both sets
A = {1,2,3,4}
B = {3,4,5,6}
print(A | B)

# Intersection
# is a set of elements that are common in both sets
print(A & B)

# Difference
# A and B (A-B ) is a set of elements that are only in A but not in B
print(A - B)

# letters in both a and b
print(A ^ B)