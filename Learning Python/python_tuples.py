#Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Access Tuple Item
print(thistuple[1])

#Negative Indexing -> means beginning from end
print(thistuple[-1])

#Range of indexs (index starts from 0)
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# First is inclusive and last is exclusive
print(thistuple1[2:5])

#Range of negative Indexes
#It return the items from index -4(included) to index -1(excluded)
print(thistuple1[-4:-1])

#Change tuple Values
#Tuples are unchangeable or immutable
# TypeError: 'tuple' object does not support item assignmentby executing below code
# x = ("apple", "banana", "cherry")
# x[1] = "kiwi"
# print(x)

#To Change value we should convert it to the list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Loop through the tuple
thistuple2 = ("apple" ,"banana", "cherry")
for x in thistuple2:
    print(x)

#Check if Item Exists
thistuple3 = ("apple", "banana", "orange")
if "banana" in thistuple3:
    print("Yes, 'apple' is in the fruits tuple")

#Tuple Length
print(len(thistuple3))

#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# thistuple4 = ("apple", "banana", "mango")
# thistuple4[3] = "cherry"
# print(thistuple4)

#Create Tuple With One Item
thistuple5 = ("pears",)
print(type(thistuple5))
thistuple6 = ("pears")
print(type(thistuple6))

#Delete Items
#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
thistuple7 = ("apple", "banana" "pomegranate")
del thistuple7
#print(thistuple7) #this will raise an error because the tuple no longer exists

#Join two tuples
tuple1 = ("a", "b", "c")
tuple2 = ("1", "2", "3")
tuple3 = tuple1 + tuple2
print(tuple3)

#The tuple() Constructor
thistuple8 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple8)




