# print("Welcome to the tip calculator!")
#bill = float(input("What was the total bill? $"))
#tip = int(input("What percentage tip would you like to give? 10 12 15 "))
#people = int(input("How many people to split the bill? "))
#howmuchisit = (bill / people) + (bill/people*tip/100)
#print(f"Each person should pay:{howmuchisit}" )
#print(f"O calculando diferente... {round((bill * (1 + tip /100)) / people,2)}")

# Pair or none verification
print("Odd or Even Verificator!")
is_it_even = int(input("Give any integer: "))
if is_it_even == 0 or (is_it_even % 2) == 0:
    print("You gave me an even number")
else:
    print("You gave me an odd number")
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")
