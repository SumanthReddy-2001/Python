# The append() method appends an element to the end of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

# copy(): Returns a shallow copy of the list.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# clear(): Removes all elements from the list.
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# count(): Returns the number of times a specified element appears in the list.
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

# extend(): Adds elements from another list to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# index(): Returns the index of the first occurrence of a specified element.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
# insert(): Inserts an element at a specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# remove(): Removes the first occurrence of a specified element.
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# reverse(): Reverses the order of the elements in the list.
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# sort(): Sorts the list in ascending order (by default).
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

