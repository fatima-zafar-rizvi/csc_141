# 11_02_city_country.py

import pytest
from city_functions_11_02 import city_country

def test_city_country():
    """Test if the function works with just city and country."""
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    """Test if the function works with city, country, and population."""
    formatted_name = city_country('santiago', 'chile', population=5000000)
    assert formatted_name == 'Santiago, Chile – population 5000000'
