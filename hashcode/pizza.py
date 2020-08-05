import random


def randomCombination(n, type_pizzas):
    for chunk in range(0, len(type_pizzas), n):
        val = type_pizzas[chunk:chunk+n]
        if len(val) == n:
            yield tuple(val)


inputFile = "d_quite_big.in"
outFile = "d_quite_big.txt"
with open("data/input/" + inputFile, "r") as file:
    first_line: list = file.readline().split()

    pizza_slices = first_line[0]

    num_type = first_line[1]

    type_pizzas: list = file.readline().split()


# convert to int
type_pizzas = list(map(int, type_pizzas))
pizza_slices = int(pizza_slices)
num_type = int(num_type)
sums = {}

# to reduce time you can change the main loop start point to 10th of the total types (1000 items will possibly needs at least 100 different tuple to get the required slices)
# start = int(num_type / 10)

for i in range(num_type):
    # set the random Combination sets numbers
    numOfRandomCombination = 10
    # generate all possible sum combinations
    for yy in range(numOfRandomCombination):
        # shuffle(type_pizzas)
        b = random.sample(type_pizzas, len(type_pizzas))
        comb = list(randomCombination(i + 1, b))
        # find the sum for each combinations
        for tupleValue in comb:
            temp = sum(tupleValue)
            # add it to a dict which its key represents the sum while the value is the pizza types tuple
            if temp <= pizza_slices:
                sums[temp] = tupleValue
# find the max sum
bestGuess = max(sums, key=int)
closest = sums[bestGuess]
# find the index of each pizza type in the input file
ind = []
for item in closest:
    ind.append(str(type_pizzas.index(item)))
# write the data to output file
with open("data/output/" + outFile, "w") as file:
    file.write(str(len(closest)))
    file.write("\n")
    file.writelines(' '.join(ind))
