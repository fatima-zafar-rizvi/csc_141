# Challenge level 8/10
import pytest
from employee_11_03 import Employee
@pytest.fixture

def test_give_default_raise():
    # Test that the default raise adds $5,000 to the annual salary.
    employee = Employee('JJ', 'Maybank', 50000)
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise():
    # Test that the custom raise amount is added to the annual salary.
    employee = Employee('JJ', 'Maybank', 50000)
    employee.give_raise(10000)
    assert employee.annual_salary == 60000