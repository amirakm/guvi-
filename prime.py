# taking input from user
number = int(input(""))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("no")
            break
    else:
        print("yes")

# if the entered number is less than or equal to 1
# then it is not prime num
else:
    print("no")
