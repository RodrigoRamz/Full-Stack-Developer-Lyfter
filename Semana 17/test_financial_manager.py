import pytest
from Financial_Manager import FinancialManager

def test_add_transaction_rejects_title_only_spaces(tmp_path):
    file = tmp_path / "data.json"
    fm = FinancialManager(str(file))

    with pytest.raises(ValueError):
        fm.add_transaction(
            title=" ",
            amount=10,
            transaction_type="INCOME",
            date="2025-12-15",
            category="Food",
        )

def test_add_transaction_income_forces_positive_amount(tmp_path):
    file = tmp_path / "data.json"
    fm = FinancialManager(str(file))

    fm.add_transaction(
        title="Salary",
        amount=-100,
        transaction_type="INCOME",
        date="2025-12-15",
        category="Salary"
    )

    assert fm.transactions[-1].amount == 100

def test_add_transaction_expenditure_forces_negative_amount(tmp_path):
    file = tmp_path / "data.json"
    fm = FinancialManager(str(file))

    fm.add_transaction(
        title="Groceries",
        amount=50,
        transaction_type="EXPENDITURE",
        date="2025-12-15",
        category="Food"
    )

    assert fm.transactions[-1].amount == -50