ticket_price=float(input("enter the price of one tickets : "))
tickets_num=int(input("how many tickets : "))
total_price= ticket_price*tickets_num
member=input("are you a member : yes or no ")
discount= float

if member == "yes" :
    discount=ticket_price* 1/10
else:
    discount=0
    
price=ticket_price-discount
print(price)
