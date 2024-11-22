num1=100
result=num1+50  #here we created extra variable

num1=100
num1=num1+50 #num1 is repeated

num1=100  #used assignment operators
num1+=50
print(num1)

num1*=2
print("multiplication:",num1)

num1-=120
print(num1)

#A = P (1 + r / 365)365 t

deposit = 1000
interest_rate = 0.04
amount_year_1 = deposit * (1 + interest_rate)
amount_year_2 = amount_year_1 * (1 + interest_rate)
amount_year_3 = amount_year_2 * (1 + interest_rate)

print("After year 1:",amount_year_1 )
print("After year 2:",amount_year_2 )
print("After year 3:",amount_year_3 )
