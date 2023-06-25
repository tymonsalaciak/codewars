def solution(s):
    arr = []
    k = ""
    if len(s) % 2 == 0:
        for i in s:
            k +=i
            if len(k) == 2:
                arr.append(k)
                k = ""
    else:
        s += "_"
        for i in s:
            k +=i
            if len(k) == 2:
                arr.append(k)
                k = ""

    return arr

    


def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
        

import re

def solution(s):
    return re.findall(".{2}", s + "_")


def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution(""))