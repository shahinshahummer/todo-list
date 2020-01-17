
from todolist import addtask,scheduled_task,get_list

def test_add_task():
    dict = {}
    todo = {'2020-01-15': ["pay rent"]}
    assert addtask(dict,'2020-01-15', "pay rent") == todo

def test_add_task_2nd_day():
    dict = {'2020-01-15': ["pay rent"]}
    todo = {'2020-01-15': ["pay rent"], '2020-01-16': ["pay tax"]}
    assert addtask(dict,'2020-01-16', "pay tax") == todo
 
def test_add_2nd_task_same_date():
    dict = {'2020-01-15': ["pay rent"]}    
    todo = {'2020-01-15': ["pay rent", "pay tax"]}
    assert addtask(dict,'2020-01-15', "pay tax") == todo


def test_get_list():
    dict = {'2020-01-15': ["pay rent"], '2020-01-16': ["pay tax"], '2020-01-17': ["household work"],
            '2020-01-18': ["long drive"], '2020-01-19': ["presentation"],
            '2020-01-20': ["book a movie"],'2020-01-21': ["date lilly"],
            '2020-01-22': ["checkup"], '2020-01-23': ["festival"]}
    assert get_list(dict) == """2020-01-15
pay rent
lol
2020-01-16
pay tax
2020-01-17
household work
2020-01-18
long drive
2020-01-19
presentation
2020-01-20
book a movie
2020-01-21
date lilly
2020-01-22
checkup
2020-01-23
festival """






    
def test_get_scheduled_list():
    dict = {'2020-01-15': ["pay rent"], '2020-01-17': ["pay tax"]}
    assert scheduled_task(dict) == dict['2020-01-17']


def test_get_scheduled_list_blank():
    dict = {}
    assert scheduled_task(dict) == "no tasks today"
