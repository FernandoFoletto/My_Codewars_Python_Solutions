# CodeWars Python Solutions

---

## Count the smiley faces!


**Definition**

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example


```Python
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1
```

---

### Given Code


```python
def count_smileys(arr):
    pass #the number of valid smiley faces in array/list
```

---

### Solution


```python
def count_smileys(arr):
    def is_smiley(face):
        if len(face) == 2 and face[0] in [':', ';'] and face[1] in [')', 'D']:
            return True
        elif len(face) == 3 and face[0] in [':', ';'] and face[1] in ['-', '~'] and face[2] in [')', 'D']:
            return True
        else:
            return False
        
    count = 0
    for face in arr:
        if is_smiley(face):
            count += 1
    return count
```

---


[See on CodeWars.com](https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python)
