fruits={"apple","kiwi","banana","lemons","kiwi"}
print(fruits)

fruit1=set(["apple","banana","apple"])
print(fruit1)

#to add elements to existing sets
#1.add()
#2.update()
fruits.add("pine-apple")
print(fruits)

fruit1.update(["melons","gavava","avocado"])
print(fruit1)

fruits.remove("apple")
print(fruits)

fruit1.discard("melons")
print(fruit1)

temp=fruits.pop()
print(fruits)
print(temp)

fruits.clear()
print(fruits)

