user = input("Insertname : ")
pword = input("Insertpassword : ")
if user == "BB" and pword == "2077":
    print("======== Welcome to the UCA shop ========")
    print("1.MSI GP73 8RE : 35000 THB")
    print("2.MSI Modern14 I7 Series : 28000 THB")
    print("3.Acer Nitro5 : 25000 THB")
    user_selected = int(input("Select number of order 1,2,3 : Select "))
    if user_selected == 1:
        total = int(input("Quantity : "))
        price = total * 35000
        print("Price MSI GP73 8RE =",price,"THB")
    elif user_selected == 2:
        total = int(input("Quantity : "))
        price = total * 28000
        print("Price MSI Modern14 I7 Series =",price,"THB")
    elif user_selected == 3:
        total = int(input("Quantity : "))
        price = total * 25000
        print("Price Acer Nitro5 =",price,"THB")   
    else:
        print("Don't have number of order")
    print("========= Thank you for purchase =========")
else:
    print("User Or Password not correct Pls try again")   
    

        


