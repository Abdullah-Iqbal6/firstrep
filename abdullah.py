print("-*-_MATHEMATICAL FORMULAS_-*-")
print("_____________________________________")
print("Options:-")
print("1) (a + b)^2 = a^2 + 2ab + b^2")
print("2) (a - b)^2 = a^2 - 2ab + b^2")
print("3) a^2 + b^2 = (a+b)(a-b)")
print("4) a^3 + b^3 = (a+b)(a^2 + b^2 -ab)")
print("5) a^3 - b^3 = (a-b)(a^2 + b^2 +ab)")
print("6) (a+b)^3 = a^3 + 3a^2b + 3a b^2 + b^3")
print("7) (a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3")
print("8) (a+b+c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca")
print("9) (a-b-c)^2 = a^2 + b^2 + c^2 - 2ab + 2bc - 2ca")
print("_____________________________________")
option = int(input("Choose an option between (1 - 9):")) 

if option == 1:
    print("Mathematical Formula: (a + b)^2 = a^2 + 2ab + b^2")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    a = a*a + 2*a*b + b*b
    print("_____________________________________")
    print("The correct answer is : ",a)
    print("_____________________________________")
    

elif option == 2: 
    print("Mathematical Formula: (a - b)^2 = a^2 - 2ab + b^2")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    b = a*a -2*a*b + b*b
    print("_____________________________________")
    print("The correct answer is : ",b)
    print("_____________________________________")

elif option == 3:
    print("Mathematical Formula: a^2 + b^2 = (a+b)(a-b)")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    e = (a+b)*(a-b)
    print("_____________________________________")
    print("The correct answer is : ",e) 
    print("_____________________________________")

elif option == 4:
    print("Mathematical Formula: a^3 + b^3 = (a+b)(a^2 + b^2 -ab)")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    c = (a+b)*(a*a + b*b -a*b) 
    print("_____________________________________")
    print("The correct answer is : ",c)
    print("_____________________________________")

elif option == 5:
    print("Mathematical Formula: a^3 - b^3 = (a-b)(a^2 + b^2 +ab)")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    d = (a-b)*(a*a + b*b +a*b) 
    print("_____________________________________")
    print("The correct answer is : ",d)
    print("_____________________________________")

elif option == 6:
    print("Mathematical Formula: (a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    f = a*a*a + 3*a*a*b + 3*a*b*b + b*b*b
    print("_____________________________________")
    print("The correct answer is : ",f)
    print("_____________________________________")

elif option == 7:
    print("Mathematical Formula: (a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    g = a*a*a - 3*a*a*b + 3*a*b*b - b*b*b
    print("_____________________________________")
    print("The correct answer is : ",g)
    print("_____________________________________")
    
elif option == 8:
    print("Mathematical Formula: (a+b+c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca ")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    print("_____________________________________")
    c= int(input("Enter the value of c:"))
    h = a*a + b*b + c*c + 2*a*b + 2*b*c + 2*c*a
    print("_____________________________________")
    print("The correct answer is : ",h)
    print("_____________________________________")

elif option == 9:
    print("Mathematical Formula: (a-b-c)^2 = a^2 + b^2 + c^2 - 2ab + 2bc - 2ca ")
    print("_____________________________________")
    a = int(input("Enter the value of a:"))
    print("_____________________________________")
    b = int(input("Enter the value of b:"))
    print("_____________________________________")
    c= int(input("Enter the value of c:"))
    h = a*a + b*b + c*c - 2*a*b + 2*b*c - 2*c*a
    print("_____________________________________")
    print("The correct answer is : ",h)
    print("_____________________________________")
else:
    print("Plz Select a valid option")