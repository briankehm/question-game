import pip

print("Hello World")

count = 1

print(count)
print(count + 1)
print(count + 2)


def main():
    print(count)
    print(count + 1)
    print(count + 2)

print("What is your name?")
name = input()
print("Hello", name)

# exponent operator **
# remove remainder in division //
# just output remainder with %

print("What is your last name?")
name_last = input()
print("Thanks", name, name_last)

x = 100.2345
print(x)
x = round(x,2)
print(x)

print("What's your age?")
age = input()

if int(age) >= 100:
    print("You're old!")
elif int(age) >= 18:
    print("You're old enough to vote.")
else:
    print("You have",18 - int(age),"years until you can vote")

