'''
You are cheering on your favorite team. After each play,
if your team got over 10 yards further down the field,
you stand up and give your friend a high five.
If they don't move forward by at least a yard you stay quiet and say 'shh',
and if they move forward 10 yards or less,
you say 'Ra!' for every yard that they moved forward in that play.
Given the number of yards that your team moved forward, output either 'High Five'
(for over 10), 'shh' (for <1), or a string that has a 'Ra!' for every yard that they gained.
'''
distance = int(input())
if distance > 10:
    print("High Five")
elif 1 <= distance <= 10:
    print("Ra!" * distance )
elif distance < 1:
    print("shh")
