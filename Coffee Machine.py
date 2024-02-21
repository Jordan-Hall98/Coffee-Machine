from Menu import MENU, resources, coffee_art
import os

#Define function to be used when printing the report of the current stock inside the machine
def print_report():
    '''This function will print the resources currently in the machine'''
    for key in resources:
        quantity = resources[key]
        key = key.capitalize()
        print (f"{key}: {quantity}")


#Define a function that will be used to refill the machine
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
        

#Define a function that will identify the choice of drink or identify if the user has inputted an invalid request
def drink_chosen(drink):
    '''This function identifies if the request is for a drink'''
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        return drink
    else:
        print ("Invalid request. Try again")
        return False


#Define a function that will find the cost of the required drink
def choice_of_drink_cost(choice):
    '''This function returns the cost of the drink they have requested'''
    print (f"A {choice} costs ${MENU[choice]["cost"]}")
    cost = MENU[choice]["cost"]
    return cost


#Define a function that will check the coins inputted against the cost of the drink
def is_drink_paid_for(drink_cost):
    '''This function checks the money inputted against the cost of the drink'''
    sum_of_quarters = int(input("How many quarters would you like to use? ")) * 0.25
    sum_of_dimes = int(input("How many dimes would you like to use? ")) * 0.10
    sum_of_nickles = int(input("How many nickles would you like to use? ")) * 0.05
    sum_of_pennies = int(input("How many pennies would you like to use? ")) * 0.01
    total_inputted_sum = (sum_of_quarters + sum_of_dimes + sum_of_nickles + sum_of_pennies)

    #check if the user requires change, if they have paid the right amount or if they have not paid enough 
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


#Define a function that will remove the resources used in the drink from the stock of the machine
def drink_resources_used(drink_chosen):
    '''This function removes the resources from the machine once a drink has been made'''
    for key in MENU[drink_chosen]["ingredients"]:
        used_quantity = MENU[drink_chosen]["ingredients"][key]
        current_quantity_in_machine = resources[key]
        remaining_quantity = current_quantity_in_machine - used_quantity
        resources[key] = remaining_quantity
        

#Define a function that will check to see if the machine has enough resources to make the requested drink
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
    

#Clear screen ready for use
os.system('cls')

#Boolean variable to be used in loop
turned_off = False

#Coffee machine functions within this while loop
while not turned_off:
    #Print coffee art for the user to see
    print(coffee_art)

    #ask the user what they are after
    customers_choice = input("What would you like to order? 'Espresso', 'Latte' or 'Cappuccino'? or you can request a 'report' or you can 'refill' the machine. You can also 'turn off' the machine ").lower()
    
    #provide the function relating to the request of the user
    if customers_choice == "report":
        print_report()
    elif customers_choice == "refill":
        refill()
    elif customers_choice == "turn off":
        turned_off = True
    elif not drink_chosen(customers_choice):
        print ("")
    
    elif does_machine_have_enough_resources(customers_choice):

        cost_of_drink = (choice_of_drink_cost(customers_choice))


        make_drink = (is_drink_paid_for(cost_of_drink))

        if make_drink:
            print (f"Please enjoy your {customers_choice}")
            print ("")
            drink_resources_used(customers_choice)
        
    