name=input("Full Name:")
mail=input("Email:")
number=input("Mobile:")
age=int(input("Age:"))
valid=1
if name[0]==" " or name[len(name)-1]==" " or name.count(" ")<1:
    valid=0
if mail[0]=="@" or mail.count("@")!=1 or mail.count(".")!=1:
    valid=0
if len(number)!=10 or number.isdigit()==False or number[0]=="0":
    valid=0
if age<18 or age>60:
    valid=0
if valid==1:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")