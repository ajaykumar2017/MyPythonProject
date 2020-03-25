# Set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Access Items
"""You cannot access items in a set by referring to an index, since sets 
are unordered the items has no index. But you can loop through the set items
using a for loop, or ask if a specified value is present in a set, 
by using the in keyword."""
thisset1 = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Check if "banana" is present in the set:
thisset2 = {"apple", "banana", "cherry"}
print("banana" in thisset2)

#Change Items
#Once a set is created, you cannot change its items, but you can add new items.

#Add Items
#To add one item to a set use the add() method.
thisset3 = {"apple", "banana", "cherry"}
thisset3.add("orange")
print(thisset3)

#To add more than one item to a set use the update() method.
thisset4 = {"apple", "banana", "cherry"}
thisset4.update(["orange", "mango", "grapes"])
print(thisset4)

#Get the Length of a Set
thisset5 = {"apple", "banana", "cherry", "mango", "orange"}
print(len(thisset5))

#Remove Item
thisset6 = {"apple", "banana", "cherry"}
thisset6.remove("banana")
print(thisset6)

#Note: If the item to remove does not exist, remove() will raise an error.
# thisset7 = {"apple", "banana", "cherry"}
# thisset7.remove("mango")
# print(thisset7)

# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset8 = {"apple", "banana", "cherry"}
thisset8.discard("mango")
print(thisset8)

# Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
thisset9 = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:
thisset10 = {"apple", "banana", "cherry"}
thisset10.clear()
print(thisset10)

# The del keyword will delete the set completely:
# thisset11 = {"apple", "banana", "cherry"}
# del thisset11
# print(thisset11) #this will raise an error because the set no longer exists

#Join Two Sets
"""There are several ways to join two or more sets in Python.
You can use the union() method that returns a new set containing 
all items from both sets, or the update() method that inserts all 
the items from one set into another:"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set4 = {"a", "b" , "c"}
set5 = {1, 2, 3}
set4.update(set5)
print(set4)

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset12 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset12)

