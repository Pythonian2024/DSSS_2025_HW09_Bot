import unittest
from math_quiz import rand_int, rand_operation, implement_operation


class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val,'the random interger is not within the specified range')

    def test_rand_operation(self):
        #Test if operation generated are within expected Set of operations {+,-,*}
        for _ in range (1000):
            oper=rand_operation()
            self.assertIn(oper, ['+','-','*'], 'the random operation is not within expected set of operations')
        
        
        
    def test_implement_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, 3, '-', '2 - 3', -1),
                (4,-6, '*', '4 * -6', -24),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                self.assertEqual((implement_operation(num1, num2, operator)),(expected_problem,expected_answer),f'The problem {expected_problem} was not performed correctly')

if __name__ == "__main__":
    unittest.main()
