from sys import argv
from datetime import date 


dict = {}

def addtask(dict,date,value):
    if date in dict: 
        dict[date].append(value)
    else:
        dict[date] = [value]
    return (dict)

def get_list(dict):
    for x in dict:
        print (str(x))
        for y in dict[x]:
            print (str(y))


def scheduled_task(dict):
    if len(dict) != 0:
        currentdate = date.today()
        return(dict[str(currentdate)])
    else:
        return("no tasks today")



    
