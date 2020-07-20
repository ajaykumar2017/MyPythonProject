# Test 1
word_list = ['2', '3', '4', '4', '5', '5', '6', '6', '6', '7', '7', '7', '8', '8', '8', '8', '8',]
temp_list = []
for str1 in word_list:
    if word_list.count(str1) <= 3:
        temp_list.append(str1)
new_list = sorted(temp_list, key=temp_list.count, reverse=True)
unique_list = []
for x in new_list:
    # check if exists in unique_list or not
    if x not in unique_list:
        unique_list.append(x)
print(unique_list[-4:])

print({ ord(i) for i in 'apple' })
print([ chr(i) for i in [65, 66, 67] ])
print({0 if i%2 ==0 else 1 for i in range(8)})

# Test 2
class A:
    def __init__(self, a = 5):
        self.a = a

        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b = 0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10

x = B()
x.f1()
print(x.a,'-', x.b)

# Test 3
# class C:
#     x = 0
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         C.x += 1
#
#     def __init__(self):
#         C.x += 1
#
#     def displayCount(self):
#         print('Count : %d' % A.x)
#
#     def display(self):
#         print('a :', self.a, ' b :', self.b)
#
# a1 = C('George', 25000)
# a2 = C('John', 30000)
# a3 = C()
# a1.display()
# a2.display()
# print(C.x)

#  Test 4
class grandpa(object):
    pass

class father(grandpa):
    pass

class mother(object):
    pass

class child(mother, father):
    pass

print(child.__mro__)

# Test 5
class class1:
    a = 1

    def f1(self):
        a = 2
        class1.a += 1
        print(class1.a, end=' ')
        print(a, end=' ')

class1().f1()
class1().f1()

print(round(2067.7, 1))
