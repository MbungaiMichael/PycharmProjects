from menu import resources
from menu import MENU
print("Welcome, how may I help you\n"
      "For available resources type, report")


def report(resource):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}ml"


# def check_sufficient(resource, menu, client):
#     if resource < menu['client']:
#         return f"Sorry there is not enough {resource[client]}"

def format_data(user):
    """convert data into a printable"""
    account_w = MENU[user]['ingredients']['water']
    account_c = MENU[user]['ingredients']['coffee']
    account_cost = MENU[user]['cost']
    if user == "capuccino" or user == "latte":
        account_m = MENU[user]['ingredients']['milk']
        return f"water : {account_w} ml\nmilk {account_m}ml\ncoffee :{account_c}ml\ncost : {account_cost}"
    else:
        return f"water : {account_w}ml \ncoffee :{account_c}ml\ncost : {account_cost}"


is_coffee_served = True
while is_coffee_served:
    user_input = input("what would you like? (espresso/latte/capuccino) or off the machine: ").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "capuccino":
        print(format_data(user_input))
    if user_input == "off":
        is_coffee_served = False
    if user_input == "report":
        print(report(resources))


# check resources sufficient
# def check_sufficient(resource, menu, client):
#     if resource < menu['client']:
#         return f"Sorry there is not enough {resource[client]}"
