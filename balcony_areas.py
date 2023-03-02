#Given inputs of two strings each of which has a width and height
#Calculate which one is bigger
#determine which of two apartments has a larger balcony. 
#Both balconies are rectangles, and you have the length and width, but you need the area.
#Your inputs are two strings where the measurements for height and width are separated by a comma

astring = input()
a = astring.split(',')
area = int(a[0]) * int(a[1])
bstring = input()
b = bstring.split(',')
brea = int(b[0]) * int(b[1])

if brea > area:
    print("Apartment B")
else:
    print("Apartment A")
