from typing import List, Dict


def calculate_balance(transactions: List[Dict[str, float]]) -> float:
    balance = 0.0
    for t in transactions:
        amount = t.get("amount", 0.0)
        if t.get("type") == "income":
            balance += amount
        elif t.get("type") == "expense":
            balance -= amount
        else:
            raise ValueError(f"Неизвестный тип транзакции: {t.get('type')}")
    return round(balance, 2)


def total_by_type(transactions: List[Dict[str, float]], tx_type: str) -> float:
    if tx_type not in ("income", "expense"):
        raise ValueError("tx_type должен быть 'income' или 'expense'")
    total = sum(t["amount"] for t in transactions if t.get("type") == tx_type)
    return round(total, 2)


def savings_rate(income: float, expenses: float) -> float:
    if income <= 0:
        raise ValueError("Доход должен быть положительным")
    return round((income - expenses) / income * 100, 2)
