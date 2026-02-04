company = {
"name": "Tesla",
"founder": 'Elon Musk',
"established": 2003
}
print(company)
print("________________________________________")

print(type(company))
print("________________________________________")

print(company['name'])
print("________________________________________")

print(len(company))
print("________________________________________")

company['name'] = 'TESLAA'
print(company)
print("________________________________________")

# Add new item in dictioary
company['location'] = 'US'
print(company)
print("________________________________________")


# Another way to get item
print(company.get('name'))
print("________________________________________")

print(company.get('namee')) # namee is not defined, so we get None

company['newkey'] = 'newval'
print(company.keys())
print(company.values())
print("________________________________________")

company['newkey'] = 'newval'
print(company.keys())
print(company.values())
print("________________________________________")

student = {
'name' : 'John',
'age' : 12,
'class' : 7
}
print(student)
student.pop('class')
print(student)
print("________________________________________")

student = {
'name' : 'John',
'age' : 12,
'class' : 7
}
print(student)
del student['class']
print(student)
print("________________________________________")

tudent = {
'name' : 'John',
'age' : 12,
'class' : 7
}
print(student)
student.clear()
print(student)
print("________________________________________")

new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})
print(new)
print(type(new))
print("________________________________________")

for item in new:
   print(item)

for item in new:
   print(item, new[item])

for item, val in new.items():
    print(item, val)

for key in new.keys():
    print(key)

for xyz in new.values():
     print(xyz)
 
for key in sorted(new):
     print(key)
print("________________________________________")

company = {
    'name': 'Apple',
    'year': 1975,
    'founders': {
    'first': 'Steve Jobs',
    'second': 'Steve Wozniak'
}
}
print(company)
print(company['founders'])
print("________________________________________")

print(company['founders']['first'])
for item, val in company.items():
    print(item, val)
print("________________________________________")
    
print(type(company['founders']))
