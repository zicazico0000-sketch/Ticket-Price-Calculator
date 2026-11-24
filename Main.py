ticket_price=float(input("enter the price of one tickets : "))
tickets_num=int(input("how many tickets : "))
total_price= ticket_price*tickets_num
member=input("are you a member : yes or no ")
discount= float

if member == "yes" :
        member_discount=total_price* 0.1
else:
        member_discount=0

if total_price >= 1000:
    discount=total_price* 0.2
    member_discount=0
else:
    discount=0

all_discount=member_discount+discount

price=total_price-all_discount
print(price)

