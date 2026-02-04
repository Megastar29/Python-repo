import time

print("This program is a timer")

exit_option = ''

while exit_option.upper() != "Q":
    t = int(input("Set the time in timer (enter in seconds): "))

    while t < 0:
        print("The time can't be less than 0. Reset timer!")
        t = int(input("Set the time in timer (enter in seconds): "))

    print("Timer set")

    for i in reversed(range(1, t + 1)):
        sec = i % 60
        min = int(i / 60) % 60
        hours = int(i / 3600)
        print(f"{hours:02}:{min:02}:{sec:02}")
        time.sleep(1)

    print("Time's up!")
    exit_option = input("To exit press 'q': ")