# Collatz Sequence
print("Enter Number: ")  # instruction for user to enter a number

# created function collatz is to determine odd/even
def collatz(number):
    if number % 2 == 0:  # the number here is even
        return number // 2
    elif number % 2 == 1:  # the number here is odd
        return 3 * number + 1


number = int(input())
r = collatz(number)
print(r)

while r != 1:
    r = collatz(r)
    print(r)
