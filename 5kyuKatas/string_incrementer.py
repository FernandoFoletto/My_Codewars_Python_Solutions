#https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

x = "fo99obar0012"

def increment_string(x):
    
    numbers = ""

    for i in reversed(x):
        if i.isnumeric() == True:
            numbers += i
        else:
            break
        
    numbers = numbers[::-1]

    if numbers:
        x = x[:-len(numbers)]
        new_numbers = int(numbers) + 1
        result = x + str(new_numbers).zfill(len(numbers))
        return result    

    else:
        result = x + "1"
        
        return result

