import json
import os

default_options = {'width':800,'height':600,'type':'standart'}

def initiate():
    try:
        loaded_options = json.load(open('options.json','r'))
        options = default_options.copy()
        options.update(loaded_options)
        json.dump(options,open('options.json','w'))
    except:
        json.dump({},open('options.json','w'))
        initiate()


initiate()

os.system('python main.py')