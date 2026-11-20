"""Модуль математических операций для учебного проекта."""


def is_even(number: int) -> bool:
    """Возвращает True, если число чётное."""
    return number % 2 == 0


def safe_divide(a: float, b: float) -> float:
    """Делит a на b, выбрасывая ValueError при делении на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
