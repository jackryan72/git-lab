import unittest

from math_ops import is_even, safe_divide


class TestMathOps(unittest.TestCase):
    """Тесты функций is_even и safe_divide."""

    def test_is_even_true(self):
        """Чётное число определяется как чётное."""
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        """Нечётное число определяется как нечётное."""
        self.assertFalse(is_even(5))

    def test_safe_divide_normal(self):
        """Обычное деление возвращает ожидаемый результат."""
        self.assertEqual(safe_divide(10, 2), 5.0)

    def test_safe_divide_by_zero(self):
        """Деление на ноль выбрасывает ValueError."""
        with self.assertRaises(ValueError):
            safe_divide(10, 0)


if __name__ == "__main__":
    unittest.main()
