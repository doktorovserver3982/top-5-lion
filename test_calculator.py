import pytest
from calculator import calculate_balance, total_by_type, savings_rate


def test_balance_positive():
    assert calculate_balance([
        {"type": "income", "amount": 10000},
        {"type": "expense", "amount": 3000},
    ]) == 7000.0


def test_balance_negative():
    assert calculate_balance([
        {"type": "income", "amount": 2000},
        {"type": "expense", "amount": 5000},
    ]) == -3000.0


def test_balance_empty():
    assert calculate_balance([]) == 0.0


def test_balance_invalid_type():
    with pytest.raises(ValueError):
        calculate_balance([{"type": "gift", "amount": 100}])


def test_total_by_type_income():
    assert total_by_type([
        {"type": "income", "amount": 1000},
        {"type": "income", "amount": 2000},
        {"type": "expense", "amount": 500},
    ], "income") == 3000.0


def test_total_by_type_expense():
    assert total_by_type([
        {"type": "income", "amount": 1000},
        {"type": "expense", "amount": 400},
        {"type": "expense", "amount": 600},
    ], "expense") == 1000.0


def test_savings_rate_normal():
    assert savings_rate(5000, 3000) == 40.0


def test_savings_rate_zero_income():
    with pytest.raises(ValueError):
        savings_rate(0, 100)
