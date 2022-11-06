code ="0805"

for x in range(3):
    y=input("Enter the pin code: ")
    if y == code:
        print("You entered correct PIN.")
        quit()
    else:
        print("Incorrect...")
print("Sorry, your payment card has been blocked.")
quit()
  
