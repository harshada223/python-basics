thisset = {"apple", "banana", "cherry"}
print(thisset)
print("________________________________________")

thisset = {"apple", "banana", "cherry", "apple"} #duplicate values are ingored
print(thisset)
print("________________________________________")

thisset = {"apple", "banana", "cherry", True, 1, 2} #The values True and 1 are considered the same value in sets, and are treated as duplicates,  The values False and 0 are considered the same value in sets, and are treated as duplicates
print(thisset)
print("________________________________________")

print("\n length of string")
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
print("________________________________________")

print("\n Set Item-Datatypes")
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print("________________________________________")

myset = {"apple", "banana", "cherry"}
print(type(myset))
print("________________________________________")

print("\n set()  constructor")
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
print("________________________________________")

print("\n Access set items")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
print("________________________________________")

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
print("________________________________________")

print("\n Add items in set")
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
print("________________________________________")

print("\n Add sets") #To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print("________________________________________")

print("\n Add any iterable") #The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
print("________________________________________")

print("\n remove items")
print("\n  If the item to remove does not exist, remove() will raise an error")
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

print("\n If the item to remove does not exist, discard() will NOT raise an error.")
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

print("\n Sets are unordered, so when using the pop() method, you do not know which item that gets removed.")
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

print("\n The clear() method empties the set")
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
print("________________________________________")

print("\n Join sets")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

print("\n")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

print("\n join multiple sets")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

print("\n")
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
print("________________________________________")

print("\n intersection")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

print("\n")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)
print("________________________________________")

print("\n Difference")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

print("\n")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
print("________________________________________")

print("\n Symmetric difference")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

print("\n")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)