'''Python code that print 
    1-Bit Wise opperators
    2-Arithmatic opperators
    3-Relation Between two Variables
'''
#Take Two Num From User
Num1 = int(input("Please enter Num 1: "))
Num2 = int(input("Please enter Num 2: "))

#Bit Wise opperators
print(str(Num1) +"|"+str(Num2)+"="+str(bin(Num1 | Num2)))
print(str(Num1) +"&"+str(Num2)+"="+str(bin(Num1 & Num2)))
print(str(Num1) +"^"+str(Num2)+"="+str(bin(Num1 ^ Num2)))
print("~"+str(Num2)+"="+str(~Num1))

#Arithmatic opperators
print(str(Num1) +"+"+str(Num2)+"="+str((Num1 + Num2)))
print(str(Num1) +"-"+str(Num2)+"="+str((Num1 - Num2)))
print(str(Num1) +"*"+str(Num2)+"="+str((Num1 * Num2)))
print(str(Num1) +"/"+str(Num2)+"="+str((Num1 / Num2)))

#Relation Between two Variables
print(str(Num1) +">" +str(Num2)+"="+str(Num1 > Num2))
print(str(Num1) +"=="+str(Num2)+"="+str(Num1 == Num2))
print(str(Num1) +">="+str(Num2)+"="+str(Num1 >= Num2))