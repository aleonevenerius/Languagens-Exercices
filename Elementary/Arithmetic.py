# Read two numbers and display the sum, subtraction, multiplication, and division.

a, b = float(input("First number: ")), float(input("Second number: "))

sum = a+b
sub = a+b
mul = a*b
try:
    div = a/b

except ZeroDivisionError:
    pass

print(f"{a}+{b}={sum}")
print(f"{a}-{b}={sub}")
print(f"{a}{b}={mul}")

if b == 0:
    print(f"You cannot divide {a} by 0.")
else:
    print(f"{a}/{b}={div}")
