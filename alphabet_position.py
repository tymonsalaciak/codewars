# you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

#     A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z


# Return the integer that represents the character "h":
# x = ord("h") 
# Get the character that represents the unicode 97:
# x = chr(97) 


# def alphabet_position(s):
#   return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in text.lower():
        for j in alphabet:
            if i == j:
                #print(alphabet.index(j) + 1)
                result += f"{alphabet.index(j) + 1} "
    return result[:-1]


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
