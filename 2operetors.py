num1=3
num2=5
print(num1,num2)
print(type(num1),type(num2))
print("________________________________________")

num1=3
num2=5
print(num1,num2)
print(type(num1),type(num2))
print(3**2)
print("________________________________________")

print(5//4)
print(6//3)
print(8//3)
print(9//6)
print(4//1)
print("________________________________________")

print(9%3)
print(5*3/2+1)
print("________________________________________")

print(2==2)
print(3==3)
print(3!=2)
print(3>2)
print(3>2)
print("________________________________________")

num = 4
print(num)
num += 1
print(num)
print("________________________________________")

num = 4
print(num)
print("________________________________________")

num -= 1   # is equivalent to num = num - 1
print(num) 
num = 4
num *= 2
print(num)
num = 4
num /= 2
print(num)
print("________________________________________")


print(True and True)
print(True and False)   
print(False & False)   

print(True or True)   
print(True or False)
print(False | False)  

print(not True)
print(not False)
print("________________________________________")

x = 5
print(x > 4 and x < 6)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))
print("________________________________________")

print(abs(-2))
print(abs(-2.1))

print(round(3.45))
print(round(-3.95))

print(round(3.46, 1))   
print(round(3.46, 2))   

print(round(3.469, 1))   
print(round(3.469, 2)) 
print("________________________________________")

new1 = 2.1
new2 = 0.3

print(new1 + new2)
print(new1 - new2)
print("________________________________________")

fir = 3  # int
sec = 0.1  # float
print (fir + sec)
print("________________________________________")

num1 = 'Hello'
num2 = '5'
print(num1 + num2)
print("________________________________________")

a = '2'
b = '3'
print(a, type(a))
print(b, type(b))
print('Addition = ', a+b) 
print()   
print("________________________________________")                  

a = int(a)
b = int(b)
print(a, type(a))       
print(b, type(b))      
print('Addition = ', a+b)
print("________________________________________")

#a = 'hi'
#a = int(a)    # this line will throw error (because python cannot convert 'hi' into  integer)
#print(a)  
print("________________________________________")

num = 2.0
print(type(num))
num = str(num)
print(type(num))
print("________________________________________")


num = 'True'
print(type(num))
num = bool(num)
print(type(num))
print("________________________________________")

num = input('enter some integer  -  ')   # pass some number e.g. 2
print(num)
print(type(num))
print("________________________________________")

num = input('Enter some number --- ')     # pass some number e.g. 2   
print(num, type(num))
new = int(num)            # this is called typecasting (i.e. you are changing data type of variable) (this line will give you error if you pass some text in the input box, try it!)
print(new, type(new))
print("________________________________________")

num1 = input('Enter first number:  ')
num2 = input('Enter second number:  ')
print(num1 + num2)    # this will simply append the two numbers one after the other
print(int(num1) + int(num2)) 
print("________________________________________")

x = 4
y = 3
if x > y:             # if is followed by condition which is followed by :    # That's standard syntax
  print('yes, x is indeed greater than y')  

  x = 14
y = 15
if x > y:             # if is followed by condition which is followed by :    # That's standard syntax
  print('yes, x is indeed greater than y') 
print('this statement is not part of if clause, hence there is no indent here')
print("________________________________________")

x = 14
y = 13
if x > y:             # if is followed by condition which is followed by :    # That's standard syntax
  print('yes, x is indeed greater than y') 
  print('I want to be part of if clause as well, so i have given 4 indents before print()') 
print('this statement is not part of if clause, hence there is no indent here')
print("________________________________________")

# else statement lies on the same level as if

if 4 > 5:
    print('four is greater than five')
else:
    print('four is smaller than five')
print("________________________________________")

    
height = 176
if height < 140:
    print('too short')
elif height < 180:
    print('height is ok')
else:
    print('too tall')
print("________________________________________")

    
height = 176
if height < 140:
    print('too short')
elif height < 180:
    print('height is ok')
else:
    print('too tall')
print("________________________________________")

is_subscibed = False
if is_subscribed:
    print('Thank you for the subscription!')
else:
    print('Please subscibe') 
print("________________________________________")  

is_subscibed = True
if is_subscribed:
    print('Thank you for the subscription!')
else:
    print('Please subscibe')  
print("________________________________________") 

x = 3
y = 4

if x<y and x+y>5:
    print('both statements are true')
if x<y or x>y:
    print('one of the statement is true')

if x>y and not x+y<5:
    print('both the statements must be true')
print("________________________________________")

#Nested If

x=7
if x>10:
    print('x is greater than 10')
    if x>20:
        print('x is greater than 20')
        if x>30:
            print('x is greater than 30')
        else:
            print('x is smaller than 30')
    else: 
        print('x is smaller than 20')
else:
    print('x is smaller than 10')
print("________________________________________")

x=int(input("Enter any number within range 10:"))
print(x>=3 and x<=10)