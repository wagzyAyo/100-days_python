from machine import MENU,resources
def add(a,b,c,d):
    """Returns the sum of 4 inputs"""
    return a + b + c + d


def payment():
    """Process and return payment """
    quater_value = 0.25
    dime_value = 0.10
    nickle_value = 0.05
    penny_value = 0.01
    quater = round(float(input("Make your payment in Quater: ")), 2)
    quater = quater_value * quater
    dime = round(float(input("Make your payment in Dime: ")), 2)
    dime = dime_value * dime
    nickle = round(float(input("Make your payment in Nickle: ")), 2)
    nickle = nickle_value * nickle
    penny = round(float(input("Make your payment in Penny: ")),2)
    penny = penny_value * penny
    total_payment = add(quater,dime,nickle,penny)
    total_payment = round(total_payment, 2)
    return total_payment

def cost(amount, payment):
    """Checks to amount of coffe and payment by user"""
    change = 0
    if payment >= amount:
        change =  payment - amount
        change = round(change, 2)
        print(f"coffe cost {amount}, you pay {payment} you get {change} as change")
        return payment
    elif amount < payment:
        print(f"coffe cost {amount}, you pay {payment} you get {change}")
        print("Amount not enough to make the purchase")




total_money = 0

##
latte_water = MENU["latte"]['ingridient']['water']
latte_milk = MENU["latte"]['ingridient']['milk']
latte_coffe = MENU["latte"]['ingridient']['coffe']
latte_cost = MENU['latte']["cost"]

##
expresso_water = MENU["expresso"]['ingridient']['water']
expresso_coffe = MENU["expresso"]['ingridient']['coffe']
expresso_cost = MENU['expresso']["cost"]

##
cappuccino_coffe = MENU["cappuccino"]['ingridient']['coffe']
cappuccino_water = MENU["cappuccino"]['ingridient']['water']
cappuccino_milk = MENU["cappuccino"]['ingridient']['milk']
cappuccino_cost = MENU['cappuccino']["cost"]
print(cappuccino_milk,cappuccino_cost,cappuccino_water )


water = resources["water"]
milk = resources["milk"]
coffe = resources["coffe"]
#Print Report
on = True
while on:
    resources["money"] = total_money
    

    order = input("What would you like? (expresso/latte/cappuccino) ").lower()
    if order == 'report':
        print(f"""Water: {water}ml\n
    Milk: {milk}ml\n
    Coffe: {coffe}g\n
    Money: ${resources["money"]}\n
    """)
    elif order == 'off':
        break
#Check if resources is sufficient?
    elif order == "expresso":
       
        if water >= expresso_water and coffe >= expresso_coffe:
            total_payment = payment()
            alert = cost(expresso_cost, total_payment)
            total_money += alert
            total_money = round(total_money, 2)
            water -= expresso_water
            coffe -= expresso_coffe
            print(milk,coffe,water)
        else:
            print(f"Not enough ingridient to makee {order}")
    elif order == "latte":
        if water >= latte_water and coffe >= latte_coffe and milk >= latte_milk:
            total_payment = payment()
            alert = cost(latte_cost, total_payment)
            total_money += alert
            total_money = round(total_money, 2)
            water -= latte_water
            coffe -= latte_coffe
            milk -= latte_milk
            print(milk,coffe,water)
        else:
            print(f"Not enough ingridient to makee {order}")
    elif order == "cappuccino":
        if water >= cappuccino_water and coffe >= cappuccino_coffe and milk >= cappuccino_milk:
            total_payment = payment()
            alert = cost(cappuccino_cost, total_payment)
            total_money += alert
            total_money = round(total_money, 2)
            water -=  cappuccino_water
            coffe -= cappuccino_coffe
            milk -= cappuccino_milk
            print(milk,coffe,water)
        else:
            print(f"Not enough ingridient to makee {order}")
    else:
        print("Check your order and try again")


#Process coins



#Check if transaction is successful



#Make Coffe
