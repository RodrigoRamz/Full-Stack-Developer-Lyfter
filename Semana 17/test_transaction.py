import pytest
from transaction import Transaction

def test_transaction_rejects_title_only_spaces():
    with pytest.raises(ValueError):
        Transaction(
            title="  ",
            amount=10, 
            transaction_type="INCOME",
            date="2025-12-15",
            category="Food"
        )

def test_transaction_strips_title():
    t = Transaction(
        title=" Rent ",
            amount=10, 
            transaction_type="INCOME",
            date="2025-12-15",
            category="Food" 
    )

    assert t.title == "Rent"