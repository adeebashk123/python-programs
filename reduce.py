from functools import reduce
number=[1,2,3,4,5]
result = reduce(lambda x,y:x+y, number)
print(result)
#average
number=[1,2,3,4,5]
result = reduce(lambda x,y:x+y, number)
avg=result//len(number)
print(avg)

