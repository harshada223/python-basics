def hello() : 
print('hello world')
print("________________________________________")

hello()

hello()
hello()
# Let's pass some argument to the function
def hello (name):
 print(f'hello {name}')
hello('John')
hello(12)
print("________________________________________")

print(type(hello))
print("________________________________________")

def addthis(first, second):
print(first + second)
print("________________________________________")

addthis(12,13)
print("________________________________________")


def hello_you(name):
  return (f'hello {name.upper()}')
print(hello_you('Students'))
print("________________________________________")


def hi(name):
    message = "Hi "+name  
    return message  
name = input("Enter the name:")
print(hi(name))
print("________________________________________")

def add():
    a = 40
    b = 30
    c = a+b  
    return c  
print("The sum is:", add())
print("________________________________________")

def add(a,b):
    return a+b
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Sum = ",add(a,b))
print("________________________________________")



p = int(input("Enter the principle amount? "))
r = float(input("Enter the rate of interest? "))
t = int(input("Enter the time in years? "))
print("________________________________________")

def simple_interest(p,t,r):
   return (p*t*r)/100
print("Simple Interest: ",simple_interest(p,r,t))
print("________________________________________")

def find_distance(speed, time):
   print(speed, time)
   return speed * time

d = find_distance(speed=10, time=3)
print(d)
d = find_distance(time=3, speed=10)
print(d)
d = find_distance(3,10)
print(d)