# """
# Strings - Advance - Accessing characters using []
# """
course = 'Python for Beginners'
# index ->0123456789........-1
print(course[0])  # First Character -> P
print(course[1])  # Second Character -> y

# if we try to access index with a negative sign it means index position from the last.
# So last position can be accessed in this example by course[19] or simply course[-1]
# and in the same way the second last can be accessed by course[18] or simply course[-2]
print(course[-1])  # Last Character -> s
print(course[19])  # Last Character -> s
print(course[-2])  # Second Last Character -> r
print(course[18])  # Second Last Character -> r

# We can select series of characters using [:] operator
# course[n:m] will select the characters from n to m-1 index(starting from n to m(excluding the last one).
# If we do not supply value of n, it will work with default value as 0 and it will start from 0th index
# If we do not supply value of m, it will print from nth index till the end of the string.
# If we do not supply value of n and m, it will print the complete string. THIS IS USED TO CLONE STRINGS.
print(course[0:3])  # Characters at index 0, 1, 2 (excluding index 3) -> Pyt
print(course[2:8])  # Characters at index 2, 3, 4, ..., 7 (excluding index 8) -> thon f
print(course[2:])   # Characters starting from index 2 to end of the String -> thon for Beginners
print(course[:5])   # Characters starting from index 0 (default value) to index 4 (=5-1) -> Pytho
print(course[:])    # Complete string -> Python for Beginners

another = course[:]  # It is same course[:] and course
course = 'Sukanta'
print(another)

