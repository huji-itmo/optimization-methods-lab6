import unittest
from specimen import Specimen


class TestSpecimen(unittest.TestCase):
    test_matrix = [
        [0, 4, 6, 2, 9],
        [4, 0, 3, 2, 9],
        [6, 3, 0, 5, 9],
        [2, 2, 5, 0, 8],
        [9, 9, 9, 8, 0],
    ]

    def test_returns_25(self):
        """Original test case"""
        specimen = Specimen([5, 1, 4, 2, 3])
        expected = 25
        result = specimen.get_target_function_value(self.test_matrix)
        self.assertEqual(result, expected)

    def test_sequence_12345(self):
        """Test case 1 from table"""
        specimen = Specimen([1, 2, 3, 4, 5])
        expected = 29
        result = specimen.get_target_function_value(self.test_matrix)
        self.assertEqual(result, expected)

    def test_sequence_21435(self):
        """Test case 2 from table"""
        specimen = Specimen([2, 1, 4, 3, 5])
        expected = 29
        result = specimen.get_target_function_value(self.test_matrix)
        self.assertEqual(result, expected)

    def test_sequence_54312(self):
        """Test case 3 from table"""
        specimen = Specimen([5, 4, 3, 1, 2])
        expected = 32
        result = specimen.get_target_function_value(self.test_matrix)
        self.assertEqual(result, expected)

    def test_sequence_43125(self):
        """Test case 4 from table"""
        specimen = Specimen([4, 3, 1, 2, 5])
        expected = 32
        result = specimen.get_target_function_value(self.test_matrix)
        self.assertEqual(result, expected)

    def test_split_to_three_parts(self):
        specimen = Specimen([1, 2, 3, 4, 5])
        parts = specimen.split_to_three_parts((1, 3))
        self.assertEqual(parts, [[1], [2, 3], [4, 5]])

    def test_crossover_two_empty_parts(self):
        parent1 = Specimen([1, 2, 3, 4, 5])
        parent2 = Specimen([5, 4, 3, 2, 1])
        child1, child2 = parent1.crossover_operation(parent2, (0, 5))
        self.assertEqual(child1.chromosome, [5, 4, 3, 2, 1])
        self.assertEqual(child2.chromosome, [1, 2, 3, 4, 5])

    def test_crossover_one_empty_part(self):
        parent1 = Specimen([1, 2, 3, 4, 5])
        parent2 = Specimen([5, 4, 3, 2, 1])
        child1, child2 = parent1.crossover_operation(parent2, (0, 2))
        self.assertEqual(child1.chromosome, [5, 4, 3, 1, 2])
        self.assertEqual(child2.chromosome, [1, 2, 3, 4, 5])

    def test_crossover_lecture(self):
        parent1 = Specimen([1, 2, 3, 4, 5])
        parent2 = Specimen([3, 4, 5, 2, 1])
        child1, child2 = parent1.crossover_operation(parent2, (1, 4))
        self.assertEqual(child1.chromosome, [3, 4, 5, 2, 1])
        self.assertEqual(child2.chromosome, [5, 2, 3, 4, 1])

    def test_target_function_value(self):
        specimen = Specimen([1, 2, 3, 4])
        matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
        cost = specimen.get_target_function_value(matrix)
        self.assertEqual(cost, 10 + 35 + 30 + 20)  # 1→2=10, 2→3=35, 3→4=30, 4→1=20

    def test_unique_genes_after_crossover(self):
        parent1 = Specimen([1, 2, 3, 4, 5])
        parent2 = Specimen([5, 4, 3, 2, 1])
        child1, child2 = parent1.crossover_operation(parent2, (1, 3))
        self.assertEqual(len(set(child1.chromosome)), len(child1.chromosome))
        self.assertEqual(len(set(child2.chromosome)), len(child2.chromosome))

    def test_chromosome_length_consistency(self):
        parent1 = Specimen([1, 2, 3, 4, 5])
        parent2 = Specimen([5, 4, 3, 2, 1])
        child1, child2 = parent1.crossover_operation(parent2, (1, 3))
        self.assertEqual(len(child1.chromosome), 5)
        self.assertEqual(len(child2.chromosome), 5)


if __name__ == "__main__":
    unittest.main()
