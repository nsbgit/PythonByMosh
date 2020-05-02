# """
# Strings Methods
# """

# We can do really cool things using string functions.
# FUNCTION: block of code responsible for a set of work
# METHOD: when function is associated with any object
# len() is a function, in-contrast upper() is a method

course = 'Python for Beginners course in on'
#         0123456789...

# BASIC FUNCTIONS AND METHODS:
print(f'len() => {len(course)}')
print(f'upper() = {course.upper()}')
print(f'lower() => {course.lower()}')
print(f'title() => {course.title()}')  # Returns a string which has first letter in each word as CAPITAL and the rest are as small
print(f'Original String => {course}')

# FIND METHOD:
print(course.find('n'))  # returns starting index of first occurrence of character(s){CASE_SENSITIVE} => 5
print(course.find('on'))  # 4
print(course.find('z'))  # returns -1 if the character(s) is/are not found => -1
print(course.find('fg'))  # -1

# REPLACE METHOD:
print(course.replace('Beginners', 'Absolute Beginner'))
print(course.replace('P', 'J'))
print(course.replace('xyz', 'abc'))  # if the searched string is not found it would return the original string

# IN OPERATOR:
# in operator is used to search character(s) in a given string. It returns boolean value,
# whereas find() returns starting index of character(s).
print('Python' in course)  # returns True
print('Sukanta' in course)  # returns False



