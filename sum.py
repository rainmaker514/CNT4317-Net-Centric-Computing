
num1 = int(input("What is your favorite number?"))

num2 = 0

for x in range(1, num1 + 1):
    if x % 3 == 0 or x % 5 == 0:
        num2 += x

print("Really? Mine is " + str(num2) + "!")