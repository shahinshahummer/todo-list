
from todolist import addline

def test_add_line():
    dict = {}
    todo = {'2020-01-15': ["pay rent"]}
    assert addline(dict,'2020-01-15', "pay rent") == todo

def test_add_2nd_line():
    dict = {}
    todo = {'2020-01-15': ["pay rent"]}
    addline(dict,'2020-01-15', "pay rent") == todo
    
    todo = {'2020-01-15': ["pay rent"], '2020-01-16': ["pay tax"]}
    assert addline(dict,'2020-01-16', "pay tax") == todo
 
def test_add_2nd_value():
    dict = {}
    todo = {'2020-01-15': ["pay rent"]}
    addline(dict,'2020-01-15', "pay rent") == todo
    
    todo = {'2020-01-15': ["pay rent", "pay tax"]}
    assert addline(dict,'2020-01-15', "pay tax") == todo
