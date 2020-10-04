Prime = int(input("Enter a number:"))

if Prime > 1:
    for i in range(2, Prime):
        if(Prime % i) == 0:
            print(Prime , "is not a prime number")
            print(i , "*", Prime//i, "=",Prime)
        else:
            print(Prime, "is a prime number")

        break




