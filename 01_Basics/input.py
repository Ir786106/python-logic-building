# a=int(input("Enter seconds accrouding user : "))
# print(" Minutes : ", a//60, " Seconds : ", a%60)
a= int(input("Enter number for swaping : "))
last_digit= a%10
a= (a//10)*10 + last_digit
print(" Before Swaping a : ", a)