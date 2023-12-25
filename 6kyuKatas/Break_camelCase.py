def solution(s):
    result = ""
    for letter in s:
        if letter.islower() == True:
            result += letter
        else:
            result += " "
            result += letter
    return result
