# amnt= int(input("Enter the amount:"))
# if amnt>500:
#     dis_amnt= amnt-(amnt*0.2)
#     print("You have 20% Discount")
#     print("The amount you've to pay:",dis_amnt,"rupees")
# elif amnt>250:
#     dis_amnt= amnt-(amnt*0.1)
#     print("You have 10% Discount")
#     print("The amount you've to pay:",dis_amnt,"rupees")
# elif amnt>100:
#     dis_amnt= amnt-(amnt*0.05)
#     print("You have 5% Discount")
#     print("The amount you've to pay:",dis_amnt,"rupees")
# else:

#     print("You have no Discount")


unit= int(input("Enter the number of units for this month:"))
if unit>200:
    amount= 150+((unit-200)*2)
    print("The amount you've to pay for",unit,"units is:",amount,"rupees")
elif unit>100:
    amount= 50+((unit-100)*1)
    print("The amount you've to pay for",unit,"units is:",amount,"rupees")
else:
    amount= unit*0.5
    print("The amount you've to pay for",unit,"units is:",amount,"rupees")
