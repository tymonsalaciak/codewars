def duplicate_count(text):
    import re
    count = 0
    pattern = r'[A-Za-z]|\d+{2:}' #r'([a-zA-Z])\1+'

    #result = re.findall("\w|\d+{2:}", text)
    #result = re.compile("\w|\d+{2:}", text)
    result = re.findall(pattern, text)
    return result

print(duplicate_count("abcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("aA11"))


# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -