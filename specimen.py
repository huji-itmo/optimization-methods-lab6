from ordered_set import OrderedSet as ordered_set
import random


class Specimen:
    chromosome: list[int]
    mutation_chance: float = 0.01

    def __init__(self, sequence: list[int], mutation_chance: float = 0.01):
        assert len(set(sequence)) == len(sequence)

        self.chromosome = sequence
        if mutation_chance is not None:
            self.mutation_chance = mutation_chance

    def breed_with(self, other: "Specimen") -> tuple["Specimen", "Specimen"]:
        possible_indexes = list(range(len(self.chromosome) + 1))
        first_index = random.choice(possible_indexes)
        possible_indexes.remove(first_index)
        second_index = random.choice(possible_indexes)

        assert first_index != second_index

        child1, child2 = self.crossover_operation(
            other, (min(first_index, second_index), max(first_index, second_index))
        )

        for child in [child1, child2]:
            if random.uniform(0, 1) <= self.mutation_chance:
                child.generate_mutation()

        return (child1, child2)

    def crossover_operation(
        self, other: "Specimen", split_positions: tuple[int, int]
    ) -> tuple["Specimen", "Specimen"]:
        # Split both parent chromosomes into three parts
        parent_a_parts = self.split_to_three_parts(split_positions)
        parent_b_parts = other.split_to_three_parts(split_positions)

        # Construct two children by combining parts from both parents
        child1_chromosome = []
        child2_chromosome = []

        if len(parent_a_parts[1]) >= 2 and parent_a_parts.count([]) == 0:
            child1_chromosome = list([parent_a_parts[1][1]]) + list(parent_b_parts[1])
            child2_chromosome = list([parent_b_parts[1][1]]) + list(parent_a_parts[1])
        else:
            child1_chromosome = (
                list(parent_a_parts[0])
                + list(parent_b_parts[1])
                + list(parent_a_parts[2])
            )
            child2_chromosome = (
                list(parent_b_parts[0])
                + list(parent_a_parts[1])
                + list(parent_b_parts[2])
            )

        child1_chromosome = list(
            ordered_set(
                list(child1_chromosome) + list(range(1, len(self.chromosome) + 1))
            )
        )
        child2_chromosome = list(
            ordered_set(
                list(child2_chromosome) + list(range(1, len(self.chromosome) + 1))
            )
        )

        # Return the two new Specimens
        return (
            Specimen(child1_chromosome, self.mutation_chance),
            Specimen(child2_chromosome, self.mutation_chance),
        )

    def mutate(self, swap_indexes: tuple[int, int]):
        assert swap_indexes[0] != swap_indexes[1]
        self.chromosome[swap_indexes[0]], self.chromosome[swap_indexes[1]] = (
            self.chromosome[swap_indexes[1]],
            self.chromosome[swap_indexes[0]],
        )

    def generate_mutation(self) -> None:
        possible_indexes = list(range(len(self.chromosome)))
        first_index = random.choice(possible_indexes)
        possible_indexes.remove(first_index)
        second_index = random.choice(possible_indexes)

        assert first_index != second_index

        self.mutate((min(first_index, second_index), max(first_index, second_index)))

    def split_to_three_parts(self, split_positions: tuple[int, int]) -> list[list[int]]:
        assert split_positions[0] < split_positions[1]
        assert split_positions[0] >= 0 and split_positions[1] <= len(self.chromosome)

        self_split = [
            self.chromosome[: (split_positions[0])],
            self.chromosome[(split_positions[0]) : (split_positions[1])],
            self.chromosome[(split_positions[1]) :],
        ]

        return self_split

    def get_target_function_value(self, matrix: list[list[int]]) -> int:
        n = len(self.chromosome)

        if n != len(matrix) or len(set(self.chromosome)) != n:
            print("Bad data in target function")

        if len(matrix) != len(matrix[0]):
            print("Matrix is not a square from")

        total_cost = 0
        for i in range(n):
            total_cost += matrix[self.chromosome[i % n] - 1][
                self.chromosome[(i + 1) % n] - 1
            ]

        return total_cost
