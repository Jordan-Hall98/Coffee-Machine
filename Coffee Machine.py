from Menu import MENU, resources, coffee_art
import os

def print_report():
    '''This function will print the resources currently in the machine'''
    for key in resources:
        quantity = resources[key]
        key = key.capitalize()
        print (f"{key}: {quantity}")


def refill():
    '''This function will refill the coffee machine'''
    for key in resources:
        if key == "water":
           resources[key] = 300
        elif key == "milk":
            resources[key] = 200
        else:
            resources[key] = 100
    return "Coffee machine refilled"
        

def drink_chosen(drink):
    '''This function identifies if the request is for a drink'''
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        return drink
    else:
        print ("Invalid request. Try again")
        return False


def choice_of_drink_cost(choice):
    '''This function returns the cost of the drink they have requested'''
    print (f"A {choice} costs ${MENU[choice]["cost"]}")
    cost = MENU[choice]["cost"]
    return cost


def money_required(choice):
    '''This function identifies if the request is a drink or not'''
    if choice == "report":
        print_report()
    elif not drink_chosen(choice):
        print ("Please choose another choice")
        return
    else:
        return choice_of_drink_cost(drink_chosen(choice))
        

def is_drink_paid_for(drink_cost):
    '''This function checks the money inputted against the cost of the drink'''
    sum_of_quarters = int(input("How many quarters would you like to use? ")) * 0.25
    sum_of_dimes = int(input("How many dimes would you like to use? ")) * 0.10
    sum_of_nickles = int(input("How many nickles would you like to use? ")) * 0.05
    sum_of_pennies = int(input("How many pennies would you like to use? ")) * 0.01
    total_inputted_sum = (sum_of_quarters + sum_of_dimes + sum_of_nickles + sum_of_pennies)

    if total_inputted_sum > drink_cost:
        change = round((total_inputted_sum - drink_cost),2)
        print (f"Thank you, Your change is ${change}")
        print ("")
        return True
    elif total_inputted_sum == drink_cost:
        print ("Thank you!")
        print ("")
        return True
    else:
        print ("Not enough money inputted, please replace your order") 
        print ("")
        return False


def drink_resources_used(drink_chosen):
    '''This function removes the resources from the machine once a drink has been made'''
    for key in MENU[drink_chosen]["ingredients"]:
        used_quantity = MENU[drink_chosen]["ingredients"][key]
        current_quantity_in_machine = resources[key]
        remaining_quantity = current_quantity_in_machine - used_quantity
        resources[key] = remaining_quantity
        

def does_machine_have_enough_resources(drink_chosen):
    '''This machine will compare resources of requested drink against the resources currently in the machine'''
    water_required = MENU[drink_chosen]["ingredients"]["water"]
    milk_required = MENU[drink_chosen]["ingredients"]["milk"]
    coffee_required = MENU[drink_chosen]["ingredients"]["coffee"]

    water_in_machine = resources["water"]
    milk_in_machine = resources["milk"]
    coffee_in_machine = resources["coffee"]

    if water_required > water_in_machine:
        print ("Water needs refilling in machine")
        return False
    elif milk_required > milk_in_machine:
        print ("Milk needs refilling in machine")
        return False
    elif coffee_required > coffee_in_machine:
        print ("Coffee needs refilling in machine")
        return False
    else:
        return True
    



# customers_choice = input("What would you like to order? 'Espresso', 'Latte' or 'Cappuchino'? or you can request a 'report' or you can 'refill' the machine. You can also 'turn off' the machine ").lower()   
os.system('cls')

turned_off = False

while not turned_off:
    


    print(coffee_art)


    customers_choice = input("What would you like to order? 'Espresso', 'Latte' or 'Cappuccino'? or you can request a 'report' or you can 'refill' the machine. You can also 'turn off' the machine ").lower()
    

    if customers_choice == "report":
        print_report()
    elif customers_choice == "refill":
        refill()
    elif customers_choice == "turn off":
        turned_off = True
    elif not drink_chosen(customers_choice):
        print ("")
    
    elif does_machine_have_enough_resources(customers_choice):

        cost_of_drink = (money_required(customers_choice))


        make_drink = (is_drink_paid_for(cost_of_drink))

        if make_drink:
            print (f"Please enjoy your {customers_choice}")
            print ("")
            drink_resources_used(customers_choice)
        
    