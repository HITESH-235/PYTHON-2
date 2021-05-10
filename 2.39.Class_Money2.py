#Here we will write a program to deal with money matters
#so basically we are converting one currency to another using classes and o

dict = {'inr':1,'usd':73,'gbp':103,'jbp':0.6,'dem':83}#we will be using this dict

print('usd--dollars\ngbp--pounds\njbp--yen\ndem--euro\n')#info for different currencies

class money:

    def __init__(cash,value,currency,values,currencies):

        cash.a = value
        cash.b = currency
        cash.c = values
        cash.d = currencies

    def convert(cash):

        print(end='')

def cnvrt_currency(value1,currency1,value2,currency2):

    if currency1 != 'inr':

        new_val = dict[currency1]
        value1*= new_val

    if currency2 != 'inr':

        new_val1 = dict[currency2]
        value2*= new_val1

    x1 = money(value1,'inr',value2,'inr')
    x1.convert()

    print((x1.a + x1.c),'inr')

value1 = int(input('Enter 1st Value: '))
currency1 = str(input('Enter Currency: '))

value2 = int(input('Enter 2st Value: '))
currency2 = str(input('Enter Currency: '))

cnvrt_currency(value1,currency1,value2,currency2)

print('----------------')

val = int(input('Enter the value: '))

old_currency = str(input('Enter the currency: '))

new_currency = str(input('Enter the new currency to be converted: '))

a = dict[old_currency]
b = dict[new_currency]

print(val*a/b)
