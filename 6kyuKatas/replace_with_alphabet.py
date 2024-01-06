#https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

import string

text = "The sunset sets at twelve o' clock."

def alphabet_position(text):
    result = ""
    for i in text.lower():
        if i.isalpha():
            letter_index = string.ascii_letters.index(i) +1
            letter_index = str(letter_index)
            result += letter_index + " "
    result = result.strip()
    return result

print(alphabet_position(text))