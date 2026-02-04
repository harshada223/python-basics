x=1
while x < 5:
    print(x)
    x+=1

print("________________________________________")
while True:
    name=input('Input name:')
    if name=='stop':
        break
    print("Your name is:", name)

print("________________________________________")
i=0
str1='Beautiful'
while i<len(str1):
    if str1[i]=='t':
        i+=1
        break
    print('Current Letter:', str1[i])
    i+=1