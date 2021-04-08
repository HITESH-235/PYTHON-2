#AND       |L)TRUE |L)FALSE|
#|R)TRUE   | true  | false |
#|R)FALSE  | false | true  |

#OR        |L)TRUE |L)FALSE|
#|R)TRUE   | true  | true  |
#|R)FALSE  | true  | false |

x = 5

#AND:-
print(x>0 and x<10) #Since both are true, so TRUE

print(x>0 and x==3) #Since one is false, so FALSE

#OR:-
print(x%2==0 or x%1==0) #Since one is true, so TRUE
#Remember % calculates remainder.
print(x%2==0 or x-5==1) #Since both are false, so FALSE5