class money:

    def __init__(cash,value,currency):

        cash.a = value
        cash.b = currency

    def modify(cash):

        value1 = int(input('Enter 1st Value: '))
        curr1 = str(input('Enter Currency: '))

        cash.a = value1
        cash.b = curr1

    def modify1(cash):

        value2 = int(input('Enter 2st Value: '))
        curr2 = str(input('Enter Currency: '))

        cash.a = value2
        cash.b = curr2

    def modify2(e1,e2):

        e1.modify()
        e2.modify1()

        if e1.b == e2.b:

            print(e1.a+e2.a, e1.b)

        else:

            print('currencies refused being together')

e1 = money(0,'#')
e2 = money(0,'##')

e1.modify2(e2)
