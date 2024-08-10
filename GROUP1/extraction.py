number = 123456
list1 = []
while(True): 
    digit = number % 10 
    # print(digit)
    number = int(number / 10)
    list1.append(digit)
    # print(number)
    if (number  <= 0): 
        break
    
reversed_list = list1[::-1]

print(reversed_list)