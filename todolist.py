from sys import argv
from datetime import date 


dict = {}

def addline(dict,date,value):
    if date in dict: 
        dict[date].append(value)
    else:
        dict[date] = [value]
    return (dict)

