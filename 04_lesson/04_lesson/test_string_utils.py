import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# ТЕСТЫ ДЛЯ capitalize

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("test", "Test"),       
    ("python", "Python"),  
    ("hello world", "Hello world"),  
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),               
    (" ", " "),             
    (None, None),           
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ТЕСТЫ ДЛЯ trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   SkyPro", "SkyPro"),  
    ("SkyPro", "SkyPro"),     
    (" Hello World", "Hello World"),  
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                 
    ("     ", ""),            
    (None, None),             
    (123, None),         
])
def test_trim_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(TypeError):
            string_utils.trim(input_str)
    elif isinstance(input_str, int):
        with pytest.raises(TypeError):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected


# ТЕСТЫ ДЛЯ contains

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "P", True),          
    ("SkyPro", "Pro", True),        
    ("abcdef", "bcd", True),        
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "X", False),         
    ("SkyPro", "", False),          
    ("SkyPro", None, False),        
    ("SkyPro", "SKYPRO", False),    
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# ТЕСТЫ ДЛЯ delete_symbol

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "y", "SkPro"),              
    ("SkyPro", "Pro", "Sky"),              
    ("abcdef", "cde", "abf"),              
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "xyz", "SkyPro"),           
    ("SkyPro", "", "SkyPro"),              
    ("SkyPro", None, "SkyPro"),            
    ("None", "a", "None"),           
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected