MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

off= False
if input("Do you want to switch off machine: ").lower()=="no":
  while off==False:
    inp = input("what do you want:").lower()
    if inp == 'report':
        print(f'Resources present: WATER= {resources["water"]} , MILK= {resources["milk"]} , Coffee= {resources["coffee"]}')
    elif inp in ["latte","cappuccino","espresso"]:
        money = float(input("Enter the money: "))
        ingredient=MENU[inp]["ingredients"]
        if money>=MENU[inp]["cost"] and resources["water"]>=ingredient["water"] and resources["milk"]>=ingredient["milk"] and resources["coffee"]>=ingredient["coffee"]:
            print(f"Your order is placed.Here is your change of ${(money-MENU[inp]['cost'])} Have a nice day")
            resources["water"]=resources["water"]-ingredient["water"]
            resources["milk"]=resources["milk"]-ingredient["milk"]
            resources["coffee"]=resources["coffee"]-ingredient["coffee"]
        elif money<MENU[inp]["cost"]:
            print(f"Insufficient payment received. Here is your refund of ${money}")
        else:
            if resources["water"]<ingredient["water"]:
                print(f"Insufficient water. Please refill")
            elif resources["milk"]<ingredient["milk"]:
                print(f"Insufficient milk. Please refill")
            else:
                print(f"Insufficient coffee. Please refill")
    elif inp == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
    elif inp== "switch-off":
        off= True
    else: print("Wrong input")
