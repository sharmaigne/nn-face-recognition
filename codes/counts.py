from collections import defaultdict

# Initialize counts as a dictionary with default lists
counts = defaultdict(lambda: [0, 0, 0, 0])

# Read the file
with open("failed_expressions.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        expression = parts[0]  # First part is the expression
        probabilities = list(map(float, parts[1:]))  # Convert probabilities to floats

        # Find the index of the highest probability
        max_index = probabilities.index(max(probabilities))

        # Increment the count for the expression at the max index
        counts[expression][max_index] += 1

# Print the counts for each expression
for expression, count in counts.items():
    print(f"{expression} = {count}")

