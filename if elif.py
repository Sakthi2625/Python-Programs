Marks = int(input("Enter your mark:"))
if (Marks>=90):
        print("You've secured S grade")
elif (Marks>=80):
        print("You've secured A grade")
elif (Marks>=70):
        print("You've secured B grade")
elif (Marks>=50):
        print("You've secured c grade")
elif (Marks>=35):
        print("You've secured D grade")
else:
    print("Sorry,You are failed.")

x=5
y=10
z=15
if x<y and y<z or x==5:
    print("True")
else:
    print("False") 

a=8
b=3
c=12
if a+b*c>c and c%b==0:
    print("Condition is True")
else:
    print("Condition is False")

p=4
q=2
if not(p*q==8 or p+q==5):
    print("True")
else:
    print("False")

m=7
n=14
if 5<m<10<n:
    print("True")
else:
    print("False")

r=20
s=5
t=2
if(r%s==0 and r/s>t) or (r-s*t<10):
    print("True")
else:
    print("False")

u=2
v=3
w=4
if u**v>w and w**u<20 or not(v**2==9):
    print("True")
else:
    print("False")