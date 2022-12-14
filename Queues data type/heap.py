from heapq import heappush, heappop

fruits = []

#FRUITS LIST
heappush(fruits, "orange")
heappush(fruits, "mango")
heappush(fruits, "banana")

print(fruits)

#PERSON TUPLE COMPARISON
firstPerson = ("John", "Brown", 42)
secondPerson = ("John", "Doe", 42)
thirdPerson = ("John", "Doe", 24)

print(firstPerson < secondPerson)
print(secondPerson < thirdPerson)
