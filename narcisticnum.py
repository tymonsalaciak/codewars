def narcissistic(value):
    s = len(str(value))

    sum = 0
    for i in str(value):
        i = int(i)**s
        sum+=i

    if sum  == value:
        return True
    else:
        return False


print(narcissistic(153))
print(narcissistic(1654))
print(narcissistic(122))



#  1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


# @test.it("Narcissistic numbers")
#     def narcissistic_tests():
#         test.assert_equals(narcissistic(7), True, '7 is narcissistic');
#         test.assert_equals(narcissistic(371), True, '371 is narcissistic');

#     @test.it("Not narcissistic numbers")
#     def not_narcissistic_tests():
#         test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
#         test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')