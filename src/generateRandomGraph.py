import random

# Generate random number pairs
pairs = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(100)]

# Write pairs to file
with open("random_pairs.txt", "w") as file:
    for pair in pairs:
        file.write(f"{pair[0]} {pair[1]}\n")
