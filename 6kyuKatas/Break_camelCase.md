# CodeWars Python Solutions

---

## Break camelCase


**Definition**

Complete the solution so that the function will break up camel casing, using a space between words.


```Python
solution("camelCasing")  ==  "camel Casing"
```

---

### Given Code


```python
def solution(s):
    pass
```

---

### Solution


```python
def solution(s):
    result = ""
    for letter in s:
        if letter.islower() == True:
            result += letter
        else:
            result += " "
            result += letter
    return result
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5208f99aee097e6552000148)
