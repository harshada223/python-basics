n = int(input(" Enter a number to check:"))
if n % 2 == 0:
  print("It's an even number.")
if n % 2 != 0:
  print("It's an odd number.")
if n == 0:
  print("The number is neither even nor odd. Rather you entered Zero.")
print("________________________________________")

a = int(input("Enter the Value of a: "));  
b = int(input("Enter the Value of b: "));  
c = int(input("Enter the Value of c: "));  
if a>b and a>c:  
    print("a is largest input.");  
if b>a and b>c:  
    print("b is largest input.");  
if c>a and c>b:  
    print("c is largest input.");  
print("________________________________________")

print("\n If Else")
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print("________________________________________")

print("\n If elif else")
x = 3
if x == 1:
  print('x is one')
elif x == 2:
  print('x is two')
elif x == 3:
  print('x is three')
else:
  print('x not found')
print("________________________________________")

print("\n Nested if")
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
print("________________________________________")

print("\n Shortcut")
if a > b: print("a is greater than b")