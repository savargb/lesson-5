science = int(input("Enter the marks in science"))
maths = int(input("enter the marks in Maths"))
ss = int(input("Enter the marks in social studies"))
local = int(input("Enter the marks in Local subject"))
computer = int(input("Enter the marks in computer"))

a = ((science + maths + ss + local + computer) / 500) * 100

print(a,"%")

if a>=90:
    print("You got A+")
elif a>=80 and a<90:
    print("You got A")
elif a>=70 and a<80:
    print("You got B+")
elif a>=60 and a<70:
    print("You got B")
elif a>=50 and a<60:
    print("You got C+")
else:
    print("You Failed")
    
