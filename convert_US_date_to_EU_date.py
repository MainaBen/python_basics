'''
Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY.

Task: 
Create a function that takes in a string containing a date that is in US format, and return a string of the same date converted to EU.

Input Format: 
A string that contains a date formatting 11/19/2019 or November 19, 2019.

Output Format: 
A string of the same date but in a different format: 19/11/2019.

Sample Input: 
7/26/2019

Sample Output: 
26/7/2019


'''
import re
month = {	'January': '1',
		'February':'2',
		'March': '3',
		'April':'4',
		'May':'5',
		'June':'6',
		'July':'7',
		'August':'8',
		'September':'9',
		'October':'10',
		'November':'11',
		'December':'12',		}

us_date = 'March 11, 2019'

if us_date[0].isalpha():
    date = re.sub(',', '', us_date)
    date = date.split()
             
    x = month[date[0]]
   
    newdate = date[1] + '/' + x + '/' + date[2]
    print(newdate)

    
else:
    us_date = us_date.split('/')
    neworder = [1,0,2]
    newdate = [us_date[i] for i in neworder]
    print('/'.join(newdate))
