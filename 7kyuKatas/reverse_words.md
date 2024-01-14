# CodeWars Python Solutions

---

## Reverse words


**Definition**

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
```Python
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```

---

### Given Code


```python
def filter_list(l):
    'return a new list with the strings filtered out'
```

---

### Solution


```python
def reverse_words(text):
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python)
