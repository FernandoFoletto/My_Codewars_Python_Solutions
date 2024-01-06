# CodeWars Python Solutions

---

## Replace With Alphabet Position


**Definition**

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.


```Python
alphabet_position("The sunset sets at twelve o' clock.")
```
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

---

### Given Code


```python
def alphabet_position(text):
    pass
```

---

### Solution


```python
import string

def alphabet_position(text):
    result = ""
    for i in text.lower():
        if i.isalpha():
            letter_index = string.ascii_letters.index(i) +1
            letter_index = str(letter_index)
            result += letter_index + " "
    result = result.strip()
    return result
```

---


[See on CodeWars.com](https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python)
