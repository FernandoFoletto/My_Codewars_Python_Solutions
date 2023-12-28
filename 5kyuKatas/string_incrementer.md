# CodeWars Python Solutions

---

## String incrementer


**Definition**

Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

---

### Given Code


```python
def increment_string(x):
    return x
```

---

### Solution


```python
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
```

---


[See on CodeWars.com](https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python)
