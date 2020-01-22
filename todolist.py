from sys import argv
from datetime import date 
from json import load, dump

dict = {}

def addtask(dates,msg,dict):
        key = 1
        if key in dict:
                key += 1
                dict[key] = {"date":'',"message":''}
                dict[key]["date"] = dates
                dict[key]["message"] = msg
        else:
                dict[key] = {"date":'',"message":''}
                dict[key]["date"] = dates
                dict[key]["message"] = msg
        return (dict)

def display_list(dict):
    list = ""
    if len(dict) != 0:
        for key in dict:
            list += ("\n")
            list += str(key)
            list += (".")
            list += str(dict[key]["date"])
            list += ("\t")
            list += str(dict[key]["message"])
            list += ("\n") 
    else:
        return("no tasks added")
    return(list)

def scheduled_task(dict):
    if len(dict) != 0:
        scheduled_task = ""
        for key in dict:
                if dict[key]["date"] == str(date.today()):
                        msg = dict[key]["message"]
                        scheduled_task += msg
                        scheduled_task += ("\n")
        return(scheduled_task)
    else:
        return("no tasks today")

def delete_task(number,dict):
        if number in dict:
                del dict[number]
        return(dict)


        
        
        





        
