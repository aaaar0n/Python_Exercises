# Write a Python program that accepts an integer (n) and computes
# the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

user_input = input("Enter value for n: ")
nn = int(user_input + user_input)
nnn = int(user_input + user_input + user_input)

total = int(user_input) + nn + nnn
print(total)
