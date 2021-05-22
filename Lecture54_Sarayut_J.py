def login():
    userlog = input("Pls Insert Your Name : ")
    passlog = input("Pls Insert Password  : ")
    if userlog == "BB" and passlog == "2077":
        return menu()
    else:
        return login()
def menu():
    print("----- Operator Tool -----")
    print("1. Vat   Calculator")
    print("2. Price Calculator")
    print("3. Logout")
    return menuSelect()
def menuSelect():
    userSelected = int(input("Select number of menu : "))
    if userSelected == 1:
        priceorder = int(input("Price : "))
        print("Vat7% : ",vatcu(priceorder))
        return menuSelect()
    elif userSelected == 2:
        print("Total Price =",priceCalculator())
        return menuSelect()
    elif userSelected == 3:
        return login()
def vatcu(price):
    vat = 7
    total = price+(price*vat/100)
    return total
def priceCalculator():
    price1 = int(input("1st Product Price : "))
    price2 = int(input("2nd Product Price : "))
    return vatcu(price1 + price2)

login()
