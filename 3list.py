#Basic list
courses = ['ba','bcom','bsc','ma','mcom','msc']
print(courses)
print("________________________________________")

print(type(courses))
print("________________________________________")

#Accessing List items
courses = ['ba','bcom','bsc','ma','mcom','msc']
print(courses)
print(courses[0])
print(courses[2])
print(courses[0:2])
print(courses[1:5])
print(courses[-1])
print(courses[-2])
print(courses[-3:-1])
print(courses[-3:1])
print("________________________________________")

help(list)
help(list.append)
print("________________________________________")

courses.append('BE')
print(courses)
print("________________________________________")

#To insert an element somewhere in the middle, say 3rd index

courses.insert(3,'ME')
print(courses)
print("________________________________________")

c='B.Pharm'
courses.append(c)
print(courses)
print("________________________________________")

new=['11th','12th']
courses.append(new)
print(courses)
print(courses[-1])
print("________________________________________")

courses.extend(new)
print(courses)
print("________________________________________")

courses.pop()
print(courses)
print("________________________________________")

courses.remove('ba')
print(courses)
print("________________________________________")

#courses.sort()
#print(courses)# this should give error, read below.

#Let's define new list
fruits=['mango','apple','orange','kiwi','pineapple','papaya']
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)
print("________________________________________")

nums=[12,4,2,11,1,100]
print(nums)
nums.sort()
print(nums)
print("________________________________________")

#to check length of list, use len()
countries=['Russia','India','US','Japan','Germany','Italy','Zambia']
print(len(countries))
print("________________________________________")

print(len('HELLO'))
print("________________________________________")

nums=[8,4,2,1,16]
print(max(nums))

print(min(nums))
print(sum(nums ))

print(max(countries))
print(min(countries))
print("________________________________________")

#iterating a list

countries=['Russia','India','US','Japan','Germany','Italy','Zambia']
for item in countries:
    print(item)

for x in countries:
    print(x)

for x in countries:
    print(x)
print('Now I am outside the for loop')

print("________________________________________")

for x in countries:
    print(x)
    print('Now I am inside the for loop')

for item in countries:
    print(item, len(item ))

for item in countries:
    print(item,item.upper(),len(item ))

for item in countries:
    print(f'{item}, {item.upper()}, {len(item)}')

for item in countries:
    print(f'{item} --- {item.upper()} --- {len(item)}')
print("________________________________________")

# Use enumerate() function to get index of element.
for id, item in enumerate(countries):
    print(id, item )

for index, item in enumerate(countries):
    print(index, item )
print("________________________________________")

cubes=[]
for i in range(5):
    cubes.append(i ** 3)
print(cubes)
print("________________________________________")

cubes=[]
for i in range(5):
    print("i = ", i)
    cubes.append(i ** 3)
    print("Number appended (i ** 3) = ", i ** 3)
    print("Current status of cubes list = ", cubes)
print()
print('Outside for loop')
print(cubes)
print("________________________________________")

#Nested List
fruits = [['mango','apple','pineapple'], ['sitafal', 'orange']]
print(fruits)
print(len(fruits))

print(fruits[0], type(fruits[0]))
print(fruits[1], type(fruits[1]))

print(fruits[0][0])
print(fruits[1][0])

print(fruits[0][2])