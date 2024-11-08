# 11_01_city_country.py

import pytest
from city_functions_11_01 import city_country

def test_city_country():
    # Test if the function city_country correctly formats 'city, country'.
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'