#@colors: total number of colors of paint needed
#Each color cost 5
#The costs have a tax of 10% and answer is rounded to the
#nearest whole number
#brushes and canvas cost 40


colors = int(input())
cost_colors = 5 * colors
total_cost = int(40) + cost_colors
print(round(total_cost * 1.1))

