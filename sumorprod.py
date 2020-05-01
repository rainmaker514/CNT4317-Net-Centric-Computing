def sum(num): 
    num2 = 0 
    for x in range(1, num + 1):
        num2 += x
    print("The sum is: " + str(num2))

def product(num):
    num2 = 1
    for x in range(1, num + 1):
        num2 *= x
    print("The product is: " + str(num2))

def main():
    while True:
        try:
            num = int(input("Pick a number: "))
            break
        except ValueError:
            print("Not valid, try again")



    while True:
        choice = input("Select 's' for sum or 'p' for product: ")
        if choice is 's':

            sum(num)
            break
        elif choice is 'p':
            product(num)
            break
        else:
            print("Not valid, try again. ")

main()


