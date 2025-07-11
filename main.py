from itertools import permutations
import random
from specimen import Specimen


matrix = [
    [0, 4, 5, 3, 8],
    [4, 0, 7, 6, 8],
    [5, 7, 0, 7, 9],
    [3, 6, 7, 0, 9],
    [8, 8, 9, 9, 0],
]

lecture_matrix = [
    [0, 4, 6, 2, 9],
    [4, 0, 3, 2, 9],
    [6, 3, 0, 5, 9],
    [2, 2, 5, 0, 8],
    [9, 9, 9, 8, 0],
]

POPULATION_COUNT = 4

NUMBER_OF_GENERATIONS = 10

MUTATION_PROBABILITY = 0.01

WORKING_MATRIX = matrix

if __name__ == "__main__":
    chromosome_len = len(WORKING_MATRIX)
    possible_combinations = list(
        permutations(list(range(1, chromosome_len + 1)), chromosome_len)
    )

    population = random.sample(possible_combinations, POPULATION_COUNT)
    population: list[Specimen] = [Specimen(x, MUTATION_PROBABILITY) for x in population]
    for i in range(NUMBER_OF_GENERATIONS):
        print("----------------------------------------------------")
        print("Population ", i, ": ")

        print("Parents:")
        for specimen in population:
            print(
                "".join([str(x) for x in specimen.chromosome]),
                specimen.get_target_function_value(WORKING_MATRIX),
            )

        # print("Breeding:")

        for pair_index in range(0, POPULATION_COUNT, 2):
            # print(" Pair: ", pair_index // 2)
            shuffled_population = population.copy()
            random.shuffle(shuffled_population)
            chosen_pair = shuffled_population[pair_index : pair_index + 2]

            child1, child2 = chosen_pair[0].breed_with(chosen_pair[1])

            population.append(child1)
            population.append(child2)

        population.sort(key=lambda x: x.get_target_function_value(WORKING_MATRIX))

        print("New full population:")
        for specimen in population:
            print(
                "".join([str(x) for x in specimen.chromosome]),
                specimen.get_target_function_value(WORKING_MATRIX),
            )

        population = population[0:(POPULATION_COUNT)]
        print("Deleted last", POPULATION_COUNT)

    print("best result after", NUMBER_OF_GENERATIONS, "generations:")
    print(
        "".join([str(x) for x in population[0].chromosome]),
        population[0].get_target_function_value(WORKING_MATRIX),
    )
