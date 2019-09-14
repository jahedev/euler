def q2(lst, prefix):
    matched_strings = []
    for string in lst:
        if string[:len(prefix)] == prefix:
            matched_strings.append(string)
    return matched_strings

lst = ['prenatal', 'hello', 'prehello', 'coolpre', 'preschool']
prefix = 'pre'

print(q2(lst, prefix))

def q3(string): 
    new_str = ''
    occ = 0
    for i in range(0, len(string)):
        if i == 0:
            occ = 1
            continue
        if string[i] == string[i-1]:
            occ += 1
        else:
            new_str = new_str + string[i-1] + str(occ)
            occ = 1
    new_str = new_str + string[-1] + str(occ)
    return new_str
#A4a2B1C3D2e1
print('Expected: ' + 'A4a2B1C3D2e1')
print('      Got:' + q3('AAAAaaBCCCDDe'))