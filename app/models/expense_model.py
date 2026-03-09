from pydantic import BaseModel,Field,field_validator
from datetime import date, datetime
from typing import Optional
from enum import Enum

class Category(str, Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    FUN = "Fun"
    BILLS = "Bills"
    OTHER = "Other"

class Expense(BaseModel):
    title: str = Field(min_length=1) 
    expense_description: Optional[str]=Field(default = None,max_length=255) 
    amount: float = Field(gt=0)
    category: Category
    expense_date: date

    @field_validator("expense_date",mode="before")
    def parse_date(cls,value):
        formats = [
            "%Y-%m-%d",
            "%m-%Y-%d",
            "%d-%m-%Y",
            "%m/%d/%y"
        ]
        for fmt in formats:
            try:
                return datetime.strptime(value,fmt).date() # converts into standard format [YYYY-MM-DD]
            except ValueError:
                continue
        raise ValueError("Invalid date format")
    
    @field_validator("expense_date",mode="after")
    def no_future_date(cls,value):
        if value > date.today():
            raise ValueError("Expense date cannot be in future")
        return value
