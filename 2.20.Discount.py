x = eval(input("Enter the original price :"))

y = eval(input("Enter the Discount percent :"))

z = (1-(y/100))*x

Calc = "₹{:.2f} discounted {}% is ₹{:.3f}".format(x,y,z)

print(Calc)

