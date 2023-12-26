# CodeWars Python Solutions

---

## Fake Binary


**Definition**

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

---

### Given Code


```python
def fake_bin(x):
    pass
```

---

### Solution


```python
def fake_bin(x):
    result = ""
    
    for i in x:
        i = int(i)
        if i < 5:
            i = str(i)
            result += "0"
        else:
            i = str(i)
            result += "1"
    return result 
```

---


[See on CodeWars.com](https://www.codewars.com/kata/57eae65a4321032ce000002d/python)
