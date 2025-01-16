
username=input(" Welcome, please enter your name")
print(" Hello there" + username)

#The number to check
Checknumber=1

while Checknumber <= 20:
    #print(Checknumber)
    if Checknumber % 3 == 0  and Checknumber % 5 == 0:
        print("fizzbuzz")
    elif Checknumber % 5 == 0:
        print("Buzz")
    elif Checknumber % 3 == 0:
        print("fizz")
    else:
        print(Checknumber)
    
    Checknumber+=1

if Checknumber >=20:
    print("Its 20. Game Over")
