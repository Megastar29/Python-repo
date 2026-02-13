food = []
prices = []
count = []
total = 0

product = input("Enter the name of a piece of food you wanna buy(or type 'q' or ENTER to end this list): ")

while product.upper() != "Q" and product.upper() != "":
    food.append(product)
    product = input("Enter the name of a piece of food you wanna buy(or type 'q' or ENTER to end this list): ")

for item in food:
    prices.append(float(input(f"Enter the price of {item}: ")))

for item in food:
    count.append(int(input(f"Enter the count of {item}s: ")))

for i in range(0, len(food)):
    total += count[i] * prices[i]

print(f"Total: {total}")