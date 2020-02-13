import json
def initiate():
    try:
        options_dict = json.load(open('options.json','r'))
    except:
        options_dict = {}
    if options_dict.get('initiated') != True:
        options_file = open('options.json','w')
        options_dict['initiated'] = True
        options_dict['width'] = int(input('Введите ширину вашего экрана(в пикселях)'))
        options_dict['height'] = int(input('Введите высоту вашего экрана(в пикселях)'))
        json.dump(options_dict,options_file)
    return options_dict