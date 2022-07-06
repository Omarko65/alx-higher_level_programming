#!/usr/bin/python3
'''defining add_items modules'''

import sys
'''importing sys module'''

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
'''importing load_from_json_file'''

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
'''importing save_to_json_file'''


if __name__ == "__main__":
    '''main function definition'''
    filename = "add_item.json"
    argc = len(sys.argv) - 1
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    if argc == 0:
        save_to_json_file(items, filename)
    elif argc == 1:
        items.append(sys.argv[1])
    else:
        for i in range(1, argc + 1):
            items.append(sys.argv[i])
    save_to_json_file(items, filename)
    my_list = load_from_json_file(filename)
