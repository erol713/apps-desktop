x=int(input("My secret number is: " ))
low=0
high=100
ans=int((low+high)/2)
print ("Think of a secret number!" )

yans=str(input)

while yans!="c":
    print("Is your number: " + str(ans) + " ?")

    yans = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.\
Enter 'c' to indicate I guessed correctly. "))
    if yans == "l":
        low=ans

    elif yans=="h":
        high=ans

    elif yans == "c":
        print("Game over. Your secret number was:" + str(ans))
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = int((low + high)/ 2)