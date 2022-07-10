# This function  Below now uses default parameters, it does not override the function twice
def calculate_dog_years(lastname="Doe", firstname= 'John', age=18*7):
    print("firstname " + firstname)
    print("lastname " + lastname)
    print("age " + str(age))
calculate_dog_years()
#Bonus Question
#num=int(input('select number to check '))
def is_prime(num):
    if num > 1:

        for i in range(2, num):

            if (num % i) == 0:
                print(num, "is not a prime number")

                print(i, "times", num // i, "is", num)

                break

        else:

            print(num, "is a prime number")



    else:

        print(num, "is not a prime number")
is_prime(6)