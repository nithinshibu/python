# Classic Bug Example

# Mutable operation

def add_item(list):
    list.append(100)

my_list = [1,2]
add_item(my_list)

print(my_list)

# Immutable operation 

x = 10

def change(val):
    val += 5

change(x)

print(x)  # still 10 


def add_item(tpl):
    tp1+= (100,) # creates a new tuple, doesn't modify original

my_tuple = (1,2)
add_item(my_tuple)

print(my_tuple) # still (1,2)

""" 
Key points:

In lists → append() modifies the same object (mutable)
In tuples → += creates a new object, original remains unchanged

"""

def add_item(tpl):
    print("Before:", id(tpl))
    tpl += (100,)
    print("After :", id(tpl))

my_tuple = (1, 2)
print("Original:", id(my_tuple))

add_item(my_tuple)

# will see different memory IDs, proving tuple is immutable.

a = [1, 2]
b = a
print(id(a) == id(b))  # True (same object)

""" 
id() returns the unique identity (memory address) of an object in Python.
It helps you check whether two variables are pointing to the same object or different objects.

"""