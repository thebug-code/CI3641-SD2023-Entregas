import unittest
from io import StringIO
from unittest.mock import patch
from postfix_prefix_evaluator import PrefixPostfixEvaluator


class TestCalculator(unittest.TestCase):
    # ============= Prefix =============
    def test_add_three_four_prefix(self):
        self.aider(7, "+ 3 4", False)

    def test_add_nine_two_prefix(self):
        self.aider(11, "+ 9 2", False)

    def test_add_twenty_two_prefix(self):
        self.aider(22, "+ 20 2", False)

    def test_substract_four_three_prefix(self):
        self.aider(1, "- 4 3", False)

    def test_substract_four_minus_three_prefix(self):
        self.aider(100, "- 99 -1", False)

    def test_multiply_four_three_prefix(self):
        self.aider(12, "* 4 3", False)

    def test_multiply_minus_four_thirtytwo_prefix(self):
        self.aider(-128, "* -4 32", False)

    def test_divide_four_three_prefix(self):
        self.aider(1, "/ 4 3", False)

    def test_divide_twelve_three_prefix(self):
        self.aider(4, "/ 12 3", False)

    def test_divide_minus_twelve_three_prefix(self):
        self.aider(-4, "/ -12 3", False)

    def test_add_add_four_three_four_prefix(self):
        self.aider(11, "+ + 4 3 4", False)

    def test_add_substract_four_three_four_prefix(self):
        self.aider(5, "+ - 4 3 4", False)

    def test_divide_multiply_three_four_four_prefix(self):
        self.aider(3, "/ * 3 4 4", False)

    def test_divide_add_four_four_four_prefix(self):
        self.aider(2, "/ + 4 4 4", False)

    def test_add_add_add_four_three_four_three_prefix(self):
        self.aider(14, "+ + + 4 3 4 3", False)

    def test_add_substract_substract_four_three_four_three_prefix(self):
        self.aider(0, "+ - - 4 3 4 3", False)

    def test_divide_multiply_multiply_two_two_two_eight_prefix(self):
        self.aider(1, "/ * * 2 2 2 8", False)

    def test_add_add_add_add_four_three_four_three_four_prefix(self):
        self.aider(18, "+ + + + 4 3 4 3 4", False)

    def test_divide_multiply_multiply_multiply_two_two_two_two_prefix(self):
        self.aider(1, "/ * * * 2 2 2 2 16", False)

    def test_add_add_three_four_substract_four_three_prefix(self):
        self.aider(8, "+ + 3 4 - 4 3", False)


    # ============= Postfix =============
    def test_add_three_four_postfix(self):
        self.aider(7, "3 4 +")

    def test_add_nine_two_postfix(self):
        self.aider(11, "9 2 +")

    def test_add_twenty_two_postfix(self):
        self.aider(22, "20 2 +")

    def test_substract_four_three_postfix(self):
        self.aider(1, "4 3 -")

    def test_substract_four_minus_three_postfix(self):
        self.aider(100, "99 -1 -")

    def test_multiply_four_three_postfix(self):
        self.aider(12, "4 3 *")

    def test_multiply_minus_four_thirtytwo_postfix(self):
        self.aider(-128, "-4 32 *")

    def test_divide_four_three_postfix(self):
        self.aider(1, "4 3 /")

    def test_divide_twelve_three_postfix(self):
        self.aider(4, "12 3 /")

    def test_divide_minus_twelve_three_postfix(self):
        self.aider(-4, "-12 3 /")

    def test_add_add_four_three_four_postfix(self):
        self.aider(11, "4 3 + 4 +")

    def test_add_substract_four_three_four_postfix(self):
        self.aider(5, "4 3 - 4 +")

    def test_divide_multiply_three_four_four_postfix(self):
        self.aider(3, "3 4 * 4 /")

    def test_divide_add_four_four_four_postfix(self):
        self.aider(2, "4 4 + 4 /")

    def test_add_add_add_four_three_four_three_postfix(self):
        self.aider(14, "4 3 + 4 3 + +")

    def test_add_substract_substract_four_three_four_three_postfix(self):
        self.aider(0, "4 3 - 4 3 - -")

    def test_divide_multiply_multiply_two_two_two_eight_postfix(self):
        self.aider(1, "2 2 * 2 * 8 /")

    def test_add_add_add_add_four_three_four_three_four_postfix(self):
        self.aider(18, "4 3 + 4 3 + + 4 +")

    def test_divide_multiply_multiply_multiply_two_two_two_two_postfix(self):
        self.aider(1, "2 2 * 2 * 2 * 16 /")

    def test_add_add_three_four_substract_four_three_postfix(self):
        self.aider(8, "3 4 + 4 3 - +")
    
    # ============= Show prefix expression to infix ============= 
    def test_show_prefix_expression(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("3+4", calc.prefix_to_infix("+ 3 4".split()))

    def test_show_prefix_expression_2(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("9+2", calc.prefix_to_infix("+ 9 2".split()))

    def test_show_prefix_expression_3(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("20+2", calc.prefix_to_infix("+ 20 2".split()))

    def test_show_prefix_expression_4(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4-3", calc.prefix_to_infix("- 4 3".split()))

    def test_show_prefix_expression_5(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("99--1", calc.prefix_to_infix("- 99 -1".split()))

    def test_show_prefix_expression_6(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4*3", calc.prefix_to_infix("* 4 3".split()))

    def test_show_prefix_expression_7(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("-4*32", calc.prefix_to_infix("* -4 32".split()))

    def test_show_prefix_expression_8(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4/3", calc.prefix_to_infix("/ 4 3".split()))

    def test_show_prefix_expression_9(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("12/3", calc.prefix_to_infix("/ 12 3".split()))

    def test_show_prefix_expression_10(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("-12/3", calc.prefix_to_infix("/ -12 3".split()))

    def test_show_prefix_expression_11(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4+3+4", calc.prefix_to_infix("+ + 4 3 4".split()))

    def test_show_prefix_expression_12(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4-3+4", calc.prefix_to_infix("+ - 4 3 4".split()))

    def test_show_prefix_expression_13(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("3*4/4", calc.prefix_to_infix("/ * 3 4 4".split()))

    def test_show_prefix_expression_14(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4+4/4", calc.prefix_to_infix("+ 4 / 4 4".split()))

    def test_show_prefix_expression_15(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4+3+4+3", calc.prefix_to_infix("+ + + 4 3 4 3".split()))

    def test_show_prefix_expression_16(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4-3-4+3", calc.prefix_to_infix("+ - - 4 3 4 3".split()))

    def test_show_prefix_expression_17(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("2*2*2/8", calc.prefix_to_infix("/ * * 2 2 2 8".split()))

    def test_show_prefix_expression_18(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4+3+4+3+4", calc.prefix_to_infix("+ + + + 4 3 4 3 4".split()))

    def test_show_prefix_expression_19(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("2*2*2*2/16", calc.prefix_to_infix("/ * * * 2 2 2 2 16".split()))

    def test_show_prefix_expression_20(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("3+4+4-4-3", calc.prefix_to_infix("- + + 3 4 4 - 4 3".split()))

    # ============= Show postfix expression to infix =============
    def test_show_postfix_expression(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("3+4", calc.postfix_to_infix("3 4 +".split()))

    def test_show_postfix_expression_2(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("9+2", calc.postfix_to_infix("9 2 +".split()))

    def test_show_postfix_expression_3(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("20+2", calc.postfix_to_infix("20 2 +".split()))

    def test_show_postfix_expression_4(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4-3", calc.postfix_to_infix("4 3 -".split()))

    def test_show_postfix_expression_5(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("99--1", calc.postfix_to_infix("99 -1 -".split()))

    def test_show_postfix_expression_6(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4*3", calc.postfix_to_infix("4 3 *".split()))

    def test_show_postfix_expression_7(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("-4*32", calc.postfix_to_infix("-4 32 *".split()))

    def test_show_postfix_expression_8(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4/3", calc.postfix_to_infix("4 3 /".split()))

    def test_show_postfix_expression_9(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("12/3", calc.postfix_to_infix("12 3 /".split()))
    
    def test_show_postfix_expression_10(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("-12/3", calc.postfix_to_infix("-12 3 /".split()))

    def test_show_postfix_expression_11(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4+3+4", calc.postfix_to_infix("4 3 + 4 +".split()))

    def test_show_postfix_expression_12(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4-3+4", calc.postfix_to_infix("4 3 - 4 +".split()))

    def test_show_postfix_expression_13(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("3*4/4", calc.postfix_to_infix("3 4 * 4 /".split()))

    def test_show_postfix_expression_14(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4+4/4", calc.postfix_to_infix("4 4 4 / +".split()))
    
    def test_show_postfix_expression_15(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4+3+4+3", calc.postfix_to_infix("4 3 + 4 + 3 +".split()))

    def test_show_postfix_expression_16(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4-3-4+3", calc.postfix_to_infix("4 3 - 4 - 3 +".split()))

    def test_show_postfix_expression_17(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("2*2*2/8", calc.postfix_to_infix("2 2 * 2 * 8 /".split()))

    def test_show_postfix_expression_18(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("4+3+4+3+4", calc.postfix_to_infix("4 3 + 4 + 3 + 4 +".split()))

    def test_show_postfix_expression_19(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("2*2*2*2/16", calc.postfix_to_infix("2 2 * 2 * 2 * 16 /".split()))
    
    def test_show_postfix_expression_20(self):
        calc = PrefixPostfixEvaluator()
        self.assertEqual("3+4+4-4-3", calc.postfix_to_infix("3 4 + 4 + 4 - 3 -".split()))

    # ============= Invalid expressions =============
    def test_invalid_expression(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.postfix_evaluator("3 4 + +".split())
    
    def test_invalid_expression_2(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.postfix_evaluator("3 4 + 4".split())

    def test_invalid_expression_3(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.postfix_evaluator("-12 / 3".split())
    
    def test_invalid_expression_4(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.postfix_evaluator("3 4 + 4 + 4".split())
    
    def test_invalid_expression_5(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.postfix_evaluator("+ - - 4 3 4 3 4".split())

    def test_invalid_expression_6(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.prefix_evaluator("/ * * * 2 2 2 8".split())

    def test_invalid_expression_7(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.prefix_evaluator("+ 4 4 4 4".split())
    
    def test_invalid_expression_8(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.prefix_evaluator("+ + 3 100 4 - 4 3".split())

    def test_invalid_expression_9(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.prefix_evaluator("- 4 3 4 3 4".split())

    def test_invalid_expression_10(self):
        calc = PrefixPostfixEvaluator()
        with self.assertRaises(Exception):
            calc.prefix_evaluator("/ * 12 3".split())


    def test_run_simulation(self):
        calc = PrefixPostfixEvaluator()
        invalid_input_test_cases = [
            "EVAL",
            "EVAL PRE",
            "EVAL PREE + 3 4",
            "EVAL POST",
            "EVAL POSTT + 3 4",
            "MOSTRAR POSTT + 3 4",
            "MOSTRAR PREE + 3 4",
            "MOSTRAR POST",
            "MOSTRAR EFE",
            "EFE",
            "SALE",
        ]

        with patch('builtins.input', side_effect=invalid_input_test_cases + ['SALIR']), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calc.run_program()
            output = mock_stdout.getvalue().strip()
            error_count = output.count("Opcion invalida")
            self.assertEqual(error_count, len(invalid_input_test_cases))

    def aider(self, expected, expression, postfix=True):
        calc = PrefixPostfixEvaluator()
        
        if postfix:
            actual = calc.postfix_evaluator(expression.split())
        else:
            actual = calc.prefix_evaluator(expression.split())

        self.assertEqual(expected, actual)

def run_tests():
    """
    Metodo para inicializar los test
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    run_tests()
