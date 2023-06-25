#sprawdzanie przez symetrie się nie sprawdzi 
#sprawdzanie przez cxtfry sprawdza się czesciowo



# def valid_braces(string):
#     braces = {"[" : 1,
#               "]" : 1,
#               "{" : 2,
#               "}" : 2,
#               "(" : 3,
#               ")" : 3
#               }
    
#     extra = [ "[]", "{}", "()" ]
#     #błędna metoda, najwyraźniej ma ona sprawdzać czy sie zamykają
#     #jeżeli pijawia się ( to zawsze ma się pojawić druga połowa w odpowieddniej kolejnosci jesli ) to z mety jest fałsz
    
#     arr = []
#     for j in braces.keys():
#         for i in string:
#             if i == j:
#                 arr.append(str(braces[j]))
#     for c in extra:
#         if string == c:
#             return True
#     if arr.count("1") == 2 and arr.count("2") == 2 and arr.count("3") == 2:
#         return True
#     else: 
#         return False

    # try

    # expect:
  
# test = len(string) // 2
    # s = string[:test]
    # line_to_test = ""
    # for i in s:
    #     line_to_test+= i 

    # return line_to_test



def valid_braces(string):
    left = ["(", "{", "["]
    right = [")", "}", "]"]

    if string[0] in left:
        #if
        return True
    else:
        return False

print(valid_braces("(){}[]"))
print(valid_braces("{}"))
print(valid_braces(")(}{][" ))




# "(){}[]"   =>  True


# "([{}])"   =>  True

# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False


#"([}{])" to be invalid: True should equal False
#"{}({})[]" to be valid: False should equal           True
# "(({{[[]]}}))" to be valid: False should equal      True

# ")(}{][" to be invalid: True should equal False