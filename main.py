number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
total = 0
for numbers in range(1,51):
    total += numbers
    print(total)

