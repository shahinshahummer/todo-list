
from todolist import addtask,scheduled_task,display_list,delete_task

def test_add_task():
    dict = {}
    todo ={1: {'date': '2020-01-15', 'message': 'pay rent'}}
    assert addtask('2020-01-15', "pay rent",dict) == todo

def test_add_task_2nd_day():
    dict = {1: {'date': '2020-01-15', 'message': 'pay rent'}}
    todo = {1: {'date': '2020-01-15', 'message': 'pay rent'}, 2 : {'date': '2020-01-16',
                                                                  'message': 'pay tax'}}
    assert addtask('2020-01-16', "pay tax",dict) == todo
 

def test_display_list_blank():
    dict = {}
    assert display_list(dict) == "no tasks added"

def test_display_list():
    dict = {1: {'date': '2020-01-15', 'message': 'pay rent'},2: {'date': '2020-01-16',
                                                                  'message': 'pay tax'},
                                                              3: {'date': '2020-01-17',
                                                                   'message': 'pay water'},
                                                               4: {'date': '2020-01-18',
                                                                    'message': 'movie'},
                                                                5: {'date': '2020-01-15',
                                                                     'message': 'homework'},
                                                                 6: {'date': '2020-01-20',
                                                                      'message': 'lala land'}}
    assert display_list(dict) == """
1.2020-01-15	pay rent

2.2020-01-16	pay tax

3.2020-01-17	pay water

4.2020-01-18	movie

5.2020-01-15	homework

6.2020-01-20	lala land
"""
#when you test the scheduled list, you have to give today's date to the dict and add message to it and change it in assert    
def test_get_scheduled_list():
    dict = {1: {'date': '2020-01-15', 'message': 'pay rent'},2: {'date': '2020-01-16',
                                                                  'message': 'pay tax'},
                                                              3: {'date': '2020-01-17',
                                                                   'message': 'pay water'},
                                                               4: {'date': '2020-01-18',
                                                                    'message': 'movie'},
                                                                5: {'date': '2020-01-15',
                                                                     'message': 'homework'},
                                                                 6: {'date': '2020-01-22',
                                                                      'message': 'lala land'}}
    assert scheduled_task(dict) == "lala land\n"


def test_get_scheduled_list_blank():
    dict = {}
    assert scheduled_task(dict) == "no tasks today"


def test_delete_message():
    dict = {1: {'date': '2020-01-15', 'message': 'pay rent'},
            2: {'date': '2020-01-16','message': 'pay tax'},
            3: {'date': '2020-01-17','message': 'pay water'},
            4: {'date': '2020-01-18','message': 'movie'},
            5: {'date': '2020-01-15','message': 'homework'},
            6: {'date': '2020-01-22','message': 'lala land'}}
    assert delete_task(2 ,dict) == {1: {'date': '2020-01-15', 'message': 'pay rent'},
                                    3: {'date': '2020-01-17','message': 'pay water'},
                                    4: {'date': '2020-01-18','message': 'movie'},
                                    5: {'date': '2020-01-15','message': 'homework'},
                                    6: {'date': '2020-01-22','message': 'lala land'}}
