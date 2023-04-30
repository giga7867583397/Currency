print("*********************EXCHANGE*********************")
a = input("Enter the Country to which Currency need to be converted: ")
c = int(input("Exchange rate: "))
b = input("Enter the Country whose currency is exchanged: ")
d = int(input("Amount to convert: "))
def currency_converter(c,d):
    return   c * d

print(currency_converter(c, d))