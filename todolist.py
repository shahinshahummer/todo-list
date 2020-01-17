from sys import argv
from datetime import date 


dict = {}

def addtask(dict,date,value):
    if date in dict: 
        dict[date].append(value)
    else:
        dict[date] = [value]
    return (dict)

def display_list(dict):
    list = ""
    for x in dict:
        list += ("\n")
        list += str(x)
        list += ("\n")
        for y in dict[x]:
            list += str(y)
            list += ("\n")
    return(list)

def scheduled_task(dict):
    if len(dict) != 0:
        dat = dict[str(date.today())]
        scheduled_task = ""
        for y in dat:
            scheduled_task += str(y)
            scheduled_task += ("\n")
        return(scheduled_task)
    else:
        return("no tasks today")



    
#print(scheduled_task(dict))
