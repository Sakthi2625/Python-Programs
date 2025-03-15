# x=input("Enter your name:")
# y=int(input("Enter your age:"))
# z=str(y)
# print(x+z)


# i=1
# j=0
# while i<=10:
#     if i%2==0:
#           j+=i
#     i+=1
# print(j)

# s="program"
# j=""
# # print(s[::-1])
# for i in s:
#     j=i+j
# print(j)

# if s=
# a=124
# print(a//10)
# num=int(input("Enter Number:"))
# rev=0
# while num!=0:
#     rem=num%10
#     rev=rev*10 + rem
#     num=num//10
# print(rev)

# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b
# print(a)
# # print(b)

# n= int(input("Enter a number:"))
# sum=0
# temp=n
# while n>0:
#     rem=n%10
#     sum+=rem**3
#     n//=10
# print(sum)
# if temp==sum:
#     print(temp,"is an Armstrong number")
# else:
#     print(temp,"is not an Armstrong number")



num=int(input("Enter a number:"))
temp=num
s_num=num**2
rev=0
while num!=0:
    rem=num%10
    rev=rev*10 + rem
    num=num//10
n=rev**2
rev2=0
while n!=0:
    rem2=n%10
    rev2=rev2*10 + rem2
    n=n//10
print(rev2)
if s_num==rev2:
    print(temp,"is an Adam number")
else:
    print(temp,"is not an Adam number")
