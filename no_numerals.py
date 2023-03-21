'''
Task: 
Take a phrase and replace any instances of an integer from 0-10 and replace it with the English word that corresponds to that integer.

Input Format: 
A string of the phrase in its original form (lowercase).

Output Format: 
A string of the updated phrase that has changed the numerals to words.

Sample Input: 
i need 2 pumpkins and 3 apples

Sample Output: 
i need two pumpkins and three apples

'''
numerals = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

text = "1 2 3 I'm loving you, 4 5 6 I'm missing you"
my_list = list(numerals.keys())

final_text = []
#if split is not used, the for loop will iterate over each letter rather than each word
for word in text.split():
    if word.isdigit() and int(word) in my_list:
        word = numerals[int(word)]
    final_text.append(word)

print(' '.join(final_text))
