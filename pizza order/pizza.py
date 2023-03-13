import pwinput
import datetime
from openpyxl import load_workbook
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = []
        self.total_price = price

    def add_topping(self, topping, topping_price):
        self.toppings.append((topping, topping_price))
        self.total_price += topping_price

    def show_order(self):
        print("You ordered a", self.name, "pizza with the following toppings:")
        for topping in self.toppings:
            print("-", topping[0], "($"+str(topping[1])+")")
        print("Total price: $"+str(self.total_price))

    def payment_page(self):
        print("Payment Page:\n")
        yname = input("Name: ")
        surname = input("Surname: ")
        card_numbers = input("Card numbers:")
        card_pass = pwinput.pwinput(prompt ="Card Password: ", mask="*")
        print(f"\nTotal Price: {self.total_price} $\n")
        choice = input("Do you want to complete your order and make the payment? (E/H) ")
        if choice.lower() == "e":
            print("Your order has been successfully completed. We wish you a nice day")
            nw = datetime.datetime.now()
            order_time = datetime.datetime.strftime(nw, '%c')
            print("Order Time:{}".format(order_time))
            db = [yname,surname,card_numbers,card_pass,self.name,order_time]
            workbook = load_workbook(filename="databs.xlsx")
            sheet = workbook.active
            sheet.append(db)
            workbook.save(filename="databs.xlsx")

            
        else:
            print("Your order has not been placed. If you want to make changes, return to the previous steps.")

    


    
turkish_pizza = Pizza("Turkish pizza", 10)
margarita_pizza = Pizza("Margarita pizza", 15)
plain_pizza = Pizza("Plain pizza", 8)
classic_pizza = Pizza("Classic pizza", 11)

print("Welcome to our pizza shop!")
print("Here are the pizzas we offer:")
print("1. Turkish pizza ($10)")
print("2. Margarita pizza ($15)")
print("3. Plain pizza ($8)")
print("4. Classic pizza ($11)")
choice = input("Enter the number of the pizza you want to order: ")

if choice == "1":
    pizza = turkish_pizza
    print("This pizza contains sausage, minced meat, tomato paste and red pepper")
elif choice == "2":
    pizza = margarita_pizza
    print("Margarita pizza is a Neapolitan pizza made with tomatoes, mozzarella, basil, olive oil and salt.")
elif choice == "3":
    pizza = plain_pizza
    print("Pizza contains only sausage and cheddar.")
elif choice == "4":
    pizza = classic_pizza
    print("Contains ingredients such as tomatoes, cheese, and often various other ingredients (mushrooms, onions, olives, pineapple, meat, etc.)")
else:
    print("Invalid choice. Please try again.")
    exit()


print("Here are the toppings we offer:")
print("1. Olive ($1)")
print("2. Cheese ($1.5)")
print("3. Mushroom ($0.75)")
print("4. Meat ($2)")
print("5. Onion (Free)")
print("6. Corn (Free)")
print("Enter the numbers of the toppings you want, separated by commas (e.g. 1,3,4):")
toppings_choices = input().split(",")


for choice in toppings_choices:
    if choice == "1":
        pizza.add_topping("olive", 1)
    elif choice == "2":
        pizza.add_topping("cheese", 1.5)
    elif choice == "3":
        pizza.add_topping("mushroom", 0.75)
    elif choice == "4":
        pizza.add_topping("meat", 2)
    elif choice == "5":
        pizza.add_topping("onion", 0)
    elif choice == "6":
        pizza.add_topping("corn", 0)
    else:
        print("Invalid choice. Please try again.")
        exit()

pizza.show_order()
pizza.payment_page()
