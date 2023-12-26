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


