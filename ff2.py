Total_amount=int(input("enter the amount:"))
is_member=input("enyter True if you are a member or enter false:").lower()=="true"
has_coupon=input("enter True if you have a coupon or enter false:").lower()=="true"
if Total_amount>=1000 and is_member:
    print("Discount eligible : True")
if is_member or has_coupon:
    print("Free delivery")
if not has_coupon:
    print("you don't have a coupon")


