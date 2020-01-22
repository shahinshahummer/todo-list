from sys import argv
from datetime import date 
dict =  {}
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
            #for date in dict[key]:
            list += str(dict[key]["date"])
            list += ("\t")
            #for message in dict[key]:
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
                        #for y in msg:
                        scheduled_task += msg
                        scheduled_task += ("\n")
        return(scheduled_task)
    else:
        return("no tasks today")

