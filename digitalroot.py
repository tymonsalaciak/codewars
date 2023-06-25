def digital_root(n):
    a = str(n)
    result = ""
    sum = 0
    c = 0

    for i in a:
        sum += int(i)

    if sum > 2:
        sum1 = 0
        while c < len(str(n)):
            for j in str(sum):
                sum1 += int(j)
                result += j
                c +=1
        k = " + ".join(result)
        k += f" = {sum}"
        return k

    else:
        pass

            


    

    #może odrazu sprawdzić jaka jest długość sumy cyfr i dopiero wtedy działać?

# cetl / 
    # c = 0
    # while c < z:
    #     for i in a:
    #         sum += int(i)
    #         result += i
    #         c +=1
    #     break
    #     #result += f" = {sum}"
    # k = " + ".join(result)
    # k += f" = {sum}"
    
    # if len(str(sum)) > 2:
    #     for i in str(sum):
    #         summ += int(i)
    #         result += i

    # k = " + ".join(result)
    # k += f" = {summ}"
    # return k


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
