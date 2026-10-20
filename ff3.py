products=["Laptop","Mobile","Headphones","Keyboard","Mouse"]
product_name=input("enter the product:").capitalize()
if product_name in products :
        print("product is available")
else:
        print("product is not available")