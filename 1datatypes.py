dummy='Hello World'
print(dummy)
print(type(dummy))
print("________________________________________")

num=3
another_num=3.0
print(type(num))
print(type(another_num))
print("________________________________________")

val=True
print(type(val))

print(another_num)
print(num)
print(val)
print("________________________________________")

#string basics

test='Apple\'s products are beautiful'
print(test)
print("________________________________________")

test="Apple's products are beautiful"
print(test)
print("________________________________________")

text="Hello World"
print(len(text))
print("________________________________________")

text="Hello Planet"
print(text[0])
print(text[4])
print(text[5])
print(text[6])
print("________________________________________")

text="welcome to python!"
print(text[2:5])
print(text[:2])
print(text[2:])
print("________________________________________")

text="welcome to python!"
print(type(text))
print(type(text[2:4]))
print("________________________________________")

#string functions
text="hello world!"
print(text.upper())
print(text.lower())
print(text.title())
print("________________________________________")

text='hello world'
print(text.count('1'))
print(text.count('rl'))
print(text.find('o'))
print(text.find('Z'))
print("________________________________________")

print(text)
print(text.count('H'))
print(text.find('H'))
print("________________________________________")

text='This is a beautiful world'
print(text.find('beautiful'))
print("________________________________________")

print(text. count('beautiful'))
print(text.count('is'))
print("________________________________________")

print(text.replace('world' , 'planet'))
print("________________________________________")

print(text)
print("________________________________________")

new_text=text.replace('world','planet')
print(new_text)
print(new_text)
print("________________________________________")

fruit='applllllleeeeeee'
print(fruit.replace('e','E'))
print(fruit.replace('z','E'))
print("________________________________________")

msg='   Hello World       '
print(msg)
print(msg.strip())
print("________________________________________")

print(len(msg))
print(len(msg.strip()))
print("________________________________________")

print(msg.count(''))
print(msg.strip().count(''))
print("________________________________________")

address = '102,Baker St,London'
print(address.split(','))
print("________________________________________")

test='how are you doing'
print(test.split(' '))
print("________________________________________")

output=test.split(' ')
print(output)
print(type(output))
print("________________________________________")

first='Bill'
last='Musk'
name = first + last
print(name)
print("________________________________________")

name=first+''+last
print(name)

name=first+'   '+last
print(name)
print("________________________________________")

name='{}{}'.format(first, last)
print(name)

name='{} {}'.format(first, last)
print(name)

name='   {}     {}   '.format(first,last)
print(name)

name='    {}     {}  '.format(last,first)
print(name)

name=f'{first}{last}'
print(name)

name=f'{first} {last}'
print(name)

name=f'{first}     {last}'
print(name)

name=f'{first.upper()} {last.lower()}'
print(name)
print("________________________________________")

num1 = 3
num2 = 5
print(num1,num2)
print(type(num1), type(num2))
print("________________________________________")

res = num1 + num2
print(res)
print("________________________________________")

print(num1-num2)
print(num1*num2)
print(num2 / num1)
print(num2 // num1)
print(num2 % num1)
print("________________________________________")

print(type(num2/num1))

new1 = 2.1
new2 = 0.3
print(new1+new2)
print(new1-new2)
print("________________________________________")

fir=3
sec=0.1
print(fir+sec)
print("________________________________________")

# Accepting user input

name=input('enter your name')
print(name)
print(type(name))
print("________________________________________")

text=input('Enter some text ->')
print(text.upper)
print(text.title())
print(text.find('e'))
print(text.count('e'))
print(text.replace('e','z'))
print(len(text))
