import pytest
from datetime import datetime
from app.models.expense_model import Expense


def test_valid_expense(valid_record):
    expense = Expense(**valid_record)

    assert expense.title == valid_record["title"]
    assert expense.expense_description == valid_record["expense_description"]
    assert expense.amount == valid_record["amount"]
    assert expense.category == valid_record["category"]
    expected_date = datetime.strptime(valid_record["expense_date"],"%Y-%m-%d").date()
    assert expense.expense_date == expected_date

def test_multiple_records(multiple_records):
    for record in multiple_records:
        expense = Expense(**record)  
        assert expense.title == record["title"]
        assert expense.expense_description == record["expense_description"]
        assert expense.amount == record["amount"]
        assert expense.category == record["category"]
        expected_date = datetime.strptime(record["expense_date"],"%Y-%m-%d").date()
        assert expense.expense_date == expected_date


@pytest.mark.parametrize("amount",[-10,0])
def test_invalid_amount(valid_record,amount):
    record = valid_record
    record["amount"] = amount
    with pytest.raises(Exception):
       Expense(**record)


def test_future_date(invalid_date_future):

    with pytest.raises(Exception):
        Expense(**invalid_date_future)


def test_empty_title(invalid_title_empty):

    with pytest.raises(Exception):
        Expense(**invalid_title_empty)