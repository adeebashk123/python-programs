""" Create a program that displays your name and complete mailing address formatted in
the manner that you would usually see it on the outside of an envelope. Your program
does not need to read any input from the user."""

name="adeeba"
mail_address="adeebashaikh916@gmail.com"
print(name)
print(mail_address)

"""In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places."""

small_container=2
large_container=3
small_amount=0.10
large_amount=0.25
refund=(2*0.10)+(3*0.25)
print("The total refund for returning the containers is",refund)
