'''
#You and 3 friends place orders
#Nachos and Pizza both cost $6.00. 
#A Cheeseburger meal costs $10. 
#Water is $4.00 and Coke is $5.00. Tax is 7%
#Determine the total cost of ordering four items
#If item not on menu, oder coke
#You are given a string of the four items 
#that you've been asked to order that are separated by spaces.


text = input().lower()

orders = text.split()

   
sum = 0
for x in orders:
    if x == "pizza":
        sum += 6
    elif x == "nachos":
        sum += 6
    elif x == "cheeseburger":
        sum += 10
    elif x == "water":
        sum += 4
    elif x == "coke":
        sum += 5
    else:
        sum += 5
    

result = round((sum * 1.07), 2)
print(result)
