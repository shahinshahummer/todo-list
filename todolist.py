from sys import argv
from datetime import date 
from json import load, dump
from argparse import ArgumentParser
import argparse

#json_file_path = "dict.json"
#with open(json_file_path,'r') as json_file:
#        dictload = load(json_file)
dict = {} #dictload.read().strip()
#dictdump = dump(dict ,open("dict.json", 'w'))
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
        # for key in dict:
        #         if key > number:
        #                 new_key = key - 1
        #                 dict[new_key] = dict[key]
        # del dict[key]
        return(dict)

def get_args():
        parser = ArgumentParser(description='the todolist arguments')
        group = parser.add_mutually_exclusive_group()
        parser.add_argument('functions',help='different functions')
        
        parser.add_argument('-d','--digit',help ='''The date on which you want the message to be
shown/the number of the message you want to delete''')

        parser.add_argument('-m','--message',help = 'the message you want to add')
        args = parser.parse_args()

        if args.functions == "add":
                return(addtask(args.digit,args.message,dict))
        elif args.functions == "list":
                return(display_list(dict))
        elif args.functions == "schedule":        
                return(scheduled_task(dict))
        elif args.functions == "complete":
                return(delete_task(args.digit,dict))


if __name__ == '__main__':
        get_args()
        


        
