#You are robbing a bank, but you’re not taking everything.
#You are looking for a specific item in the safety deposit boxes
#and you are going to drill into each one in order to find your item. 
#Once you find your item you can make your escape
#Determine the amount of time it will take you to find the item you are looking 
#for if it takes you 5 minutes to drill into each box.

#Input: A string that represent the items in each box that will be drilled in order (items are separated by a comma), 
#and secondly, a string of which item you are looking for.

#Output Format: An integer of the amount of time it will take for you to find your item

items = input()
my_item = input()

items_in_box = items.split(',')


index = items_in_box.index(my_item )
print(5*(index + 1))
