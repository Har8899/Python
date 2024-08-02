# For voting System

age = int(input("Insert your age:"))

if age >= 18:
    print("Vote")
else:
    print("Can not Vote")

# method 2

age = int(input("Insert your age:"))

result = "Vote" if age >= 18 else "Can not vote"

print(result)
# Can use this also
print("Vote") if age >= 18 else print("Can not vote")
