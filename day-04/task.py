import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(f"Haciendo random.choice: ",random.choice(friends))
suerte = random.randint(0,5)
print("Haciendo randomint: ", friends[suerte])
print("Haciendo todo en una línea: ", friends[random.randint(0,5)])
