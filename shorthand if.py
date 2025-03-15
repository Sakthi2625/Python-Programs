#if:
x=90
y=20
if x>y : print("x is greater")

# if else:
print("90") if x>y else print("20")

#else if:
print("90") if x<y else print("E") if x==y else print("20")

#Example:

m=int(input("Enter Mark:"))

print("S grade") if m>90 else print("A grade") if m>80 else print("B grade") if m>70 else print("C grade") if m>50 else print ("D grade") if m>=35 else print("Fail")