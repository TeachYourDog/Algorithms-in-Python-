

def euclid(m,n):
    if m >= n:

        r = m % n
        print(m," %  ",n," = ", r )

        while r != 0:
            m = n
            n = r
            r = m % n
            print(m," %  ",n," = ", r )



        print("The greatest common divisor of ", first_integer, " and ", second_integer, " is ", n, "!")

        if n == 1:
            print("Whoa! ", first_integer, " and ", second_integer, " are relatively prime! That's far out!")

    else:
        print("The first integer must be greater in value than the second integer.")
        return



first_integer = input("What is the first integer?")
m = int(first_integer)

second_integer = input("What is the second integer?")
n = int(second_integer)

euclid(m,n)
