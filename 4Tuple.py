courses = ('ba', 'bcom', 'bsc')
print(courses)
print(type(courses))
print(courses[1])

print(courses.count('ba'))
print(courses.count('baa')) 
print(courses.index('bsc'))

print("________________________________________")
courses = ('ba', 'bcom', 'bsc', 'bsc', 'ba')
print(courses)
print(courses.count('bsc'))          
print(courses.index('bsc'))          
print("________________________________________")

for item in courses:     
  print(item)
print("________________________________________")

for id, item in enumerate(courses):    # enumerate() returns index along with main data. Hence you need two variables at the left (id, item). These names could be any. 
  print(id, item)
print("________________________________________")

nums = (2, 3, 4)
print(type(nums))
print("________________________________________")

data = ('ba', 2, True, 'bsc')
print(data)
print(type(data))

print(type(data[0]))
print(type(data[1]))
print(type(data[2]))
print("________________________________________")

for item in data:
  print(item, type(item))
print("________________________________________")

new = ('50')              # this will be treated as string
print(type(new))
print("________________________________________")
new1 = ('50',)            # this will be treated as tuple
print(type(new1))
print("________________________________________")

print(('a','b','c') + (1, 2, 3))
print("________________________________________")

new = ('50',)
new1 = ('apple',)
new2 = ('mango','orange')
print(new + new1 + new2)
print("________________________________________")

fruits = ('apple','mango')
print('mango' in fruits)     # return True if 'mango' is part of fruits else False. Thanks to 'IN', it comes handy many times in the real world programs. 
print('mangoes' in fruits)
print("________________________________________")

print(max(2, 1, 3, 7))
print(min(2, 1, 3, 7))
print("________________________________________")

num = [1, 2, 3, 4]
new = tuple(num)
print(num)
print(new)
print("________________________________________")

print("\n Indexes")

num = (1, 2, 3, 4, 5, 6, 7)
print(num[-1])
print(num[-2])
print(num[6])
print("________________________________________")

courses = ('ba', 'bcom', 'bsc', 'be', 'ma', 'mcom',' msc', 'me')
print(courses[3:5])   # print courses from 3rd index to 5th
print(courses[3:])   # print courses from 3rd index onwards
print(courses[:3])
print(courses[-3:]) 