price_list = {'banana' : 2.0, 'apple' : 1.5, 'watermelon' : 3.5, 'pineapple' : 2.5, 'orange' : 1.0, 'melon' : 1.2}
tax = 1/100

money = 100.0

while True:
    print("Your money is: $", money)
    print("Menu: ")
    for fruit, price in price_list.items():
        print(f"{fruit.capitalize()} : ${price}")
    print("It has a tax around 5%")
    msg = str(input("Please input your order: " )).lower()
    print("If you wanna leave, type 'exit' or 'leave' or 'quit' ")

    if msg.lower() in price_list:
        try:
            msg2 = int(input("Please input the amount (use number only for a valid choice): "))
            if msg2 > 0:
                raw_total = price_list[msg] * msg2
                new_total = raw_total * tax + raw_total
                if money >= new_total:
                    print("Raw Total (Without Taxes): $", raw_total)
                    taxes = raw_total * tax
                    print("The taxes: $", taxes)
                    print("So your total for your order is: $", new_total)
                    money -= new_total
                else:
                    print("Not enough money!")
            else:
                print("Invalid Quantity!")
        except ValueError:
            print("Enter a valid amount! ")      
    elif msg.lower() == "exit" or msg.lower() == "quit" or msg.lower() == "leave":
        print("Thanks for shopping!")
        break
    else:
        print("Please input the valid order choice")