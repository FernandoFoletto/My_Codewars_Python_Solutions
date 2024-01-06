
arr = [':D',':~)',';~D',':)']

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
        

print(count_smileys(arr))