import pytest
from app.models.expense_model import Category
from app.db import get_db_connection

@pytest.fixture
def connection():
    conn = get_db_connection()
    yield conn 
    conn.close()

@pytest.fixture
def clean_expenses_table(connection):

    cursor = connection.cursor()
    cursor.execute("DELETE FROM expenses")
    connection.commit()
    cursor.close()


@pytest.fixture
def valid_record():
    return {
        "title": "Electricity Bill",
        "expense_description": "Monthly bill",
        "amount": 500,
        "category": Category.BILLS,
        "expense_date": "2026-03-02"
    }
        
@pytest.fixture
def multiple_records():
    return[
        {
            "title": "Electricity Bill",
            "expense_description": "Monthly bill",
            "amount": 500,
            "category": Category.BILLS,
            "expense_date": "2026-03-02"
        },
        {
            "title": "Lunch",
            "expense_description": "Office lunch",
            "amount": 200,
            "category": Category.FOOD,
            "expense_date": "2026-03-03"
        }
    ]

@pytest.fixture
def invalid_title_empty():
    return { "title": "",
            "expense_description": "Empty title",
            "amount": 200,
            "category": "Food",
            "expense_date": "2026-03-02"}
    

@pytest.fixture
def invalid_date_future():
    return { "title": "Future expense",
            "expense_description": "Invalid date",
            "amount": 200,
            "category": "Food",
            "expense_date": "2027-03-02"}
    