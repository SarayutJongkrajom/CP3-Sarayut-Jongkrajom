def vatcul(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
inputnum = int(input("Price = "))
print(vatcul(inputnum))