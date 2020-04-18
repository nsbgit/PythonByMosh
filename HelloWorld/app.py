#Type Convertion
birth_year = input('Birth year: ') #always return from input is string -> '1994'
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)