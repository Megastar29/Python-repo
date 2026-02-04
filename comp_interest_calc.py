print("This program is compound interest calculator")

p = float(input("Enter the percentage: "))

while p < 0:
    print("The percentage can't be negative. Try again!")
    p = float(input("Enter the percentage: "))

t = int(input("Enter the count of years: "))

while t < 0:
    print("The count of years can't be negative. Try again!")
    t = int(input("Enter the count of years: "))

A0 = float(input("Enter the amount of money: "))

while A0 < 0:
    print("The amount of money can't be negative. Try again!")
    A0 = float(input("Enter the amount of money: "))

A = A0 * (pow((1 + p / 100), t))

print(f"Final amount of money: {A:.2f}")