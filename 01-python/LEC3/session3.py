
myfile = open(r"G:\eng abd elghafar\iti_4month\Linuxx\file.txt","w")
myfile.write("My Name is Hager Badr\n")
myfile.write("My Birth Date is 14 October\n")
myfile.write("Graduated from PHI")

myfile = open("file.txt","r")

print(myfile.read())

