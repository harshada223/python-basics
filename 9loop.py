courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
    print(course)
print("________________________________________")

company={'name':'Tesla','founder':'Elon','year':2003}
for item in company:
    print(item, company[item])
print("________________________________________")

for i in range(5):   # prints from 0 to 4
  print(i)
print('------------')
for i in range(3,8):   # prints from 3 to 7
  print(i)
print("________________________________________")

courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
    if course == 'bcom':
        print(course)
    else:
        print('Course is NOT bcom')
print("________________________________________")

print("\nbreak statement")
courses = ['ba', 'bcom', 'bsc', 'be']
for item in courses:
  print(item)
  if item == 'bsc':                
    break
print("________________________________________")

print("\n continue statement")
courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
  if course == 'bsc':
    continue
  print(course)
print("________________________________________")

num = [1, 2, 3, 4, 5, 6, 7]
def sqr(item):
  return item * item
for i in num:
  print(i, sqr(i))
print("________________________________________")

rows = int(input("Enter the rows  :"))    # e.g. 3
for i in range(0, rows+1):               # Outer loop will print number of rows   (+1 because range excludes the second number)
    for j in range(i):                   # Inner loop will print number of Astrisk  
        print("*", end='')               # print() can take different arguments, by default end='\n' i.e. new line
    print() 
print("________________________________________")

# How to check length of list if there was no len() function
nums = [11,23,30,43]  
count = 0;  
for item in nums:  
    count = count + 1
print("Total length - ",count)
print("________________________________________")

nums = [11,23,30,43]  
count = 0;  
for item in nums:  
    count = count + 1
    if item == 30:  
        print("item matched")  
        break
print("found at", count, "location")