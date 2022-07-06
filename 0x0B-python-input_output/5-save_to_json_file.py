#!/us/bin/python3
'''Module definiton sav save_to_json_file'''


import json
'''importing json to the module'''


def save_to_json_file(my_obj, filename):
    '''save_to_json_file: a function that saves an obj to file using json
    Args:
        My_obj: is the object to be added to file
        filename: is the name of the file
    '''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
