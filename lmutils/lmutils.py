import os
from pprint import pprint
from getpass import getpass
import yaml
import time
import json
from random import randint
import csv

def cls():
    os.system("clear")

def p(var):
    print(var)

def pt(var):
    print(type(var))

def pp(var):
    pprint(var)

def json_file_to_csv(jsonfile, output_filename):
    """
    Takes a json file and builds a CSV file from it
    Assumptions: Json file is list of dicts

    Args:
    jsonfile: full path to json file
    output_filename: name of csv file that gets output
    """
    with open(jsonfile, 'r') as infile:
        json_data = json.load(infile)
        infile.close()
    csv_headers = list(json_data[0].keys())
    with open(output_filename, 'w', newline='') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=csv_headers)
        writer.writeheader()
        writer.writerows(json_data)
        csv_out.close()

def dict_to_yaml(source_dict):
    """
    dict_to_yaml(source_dict)

    Description: takes in a dictionary and makes yaml formatted data

    Returns YAML dictionary
    """
    yaml_dict = yaml.dump(source_dict)
    return yaml_dict

def csv_to_data(source_csv_file):
    """
    Takes source_csv_file and returns as a list of dicts.

    Args:
    source_csv_file: provide path to csv file to ingest

    Returns:
    list of dicts from source_csv_file
    """
    data = []
    with open(source_csv_file, 'r') as f:
        loaded_data = csv.DictReader(f)
        for row in loaded_data:
            data.append(row)
    return data

def list_to_yaml(source_list):
    """
    list_to_yaml(source_list)

    Description: Takes in a list and converts it to YML

    returns list from input as YAML text
    """
    yaml_list = yaml.dump(source_list)
    return yaml_list

def yaml_to_data(yaml_block):
    """
    yaml_to_data(yaml_block)

    Description: takes yaml as input and returns it as python data
    """
    converted_yaml = yaml.safe_load(yaml_block)
    return converted_yaml

def random_int():
    random = randint(100,999)
    return random

def data_to_text_file(data, text_out_file):
    """
    data_to_text_file(data, text_out_file):

    -- Description: Takes string as input and writes out to text file

    -- Arguments
    data: input string

    text_out_file: file name for output file
    """
    with open(text_out_file, 'w') as f:
        f.write(data)
    f.close()

def data_to_json_file(data, json_out_file):
    file_name = json_out_file
    with open(str(file_name), 'w') as f:
        json.dump(data, f, indent=2)

def data_from_json_file(json_in_file):
    """
    data_from_json_file(json_in_file)

    -- Description: Takes in json file and ingests it as python data
    """
    with open(json_in_file, 'r') as inf:
        json_data = json.load(inf)
        inf.close()
    return json_data

def ts():
    """
    Description: Returns current timestamp
    """
    ts = time.strftime("%Y%m%d-%H%M%S")
    return ts

def lines_from_file(file):
    """
    Description: Opens file and makes a list from the lines
    """
    with open(file, 'r') as f:
        data = f.readlines()
    return data

def block_from_file(file):
    """
    Description: Opens a file and makes a long string from the text
    """
    with open(file, 'r') as f:
        data = f.read()
    return data

def pause_and_quote(): #Pause and Quit
    input(f"[DEBUG] :: Paused... Press [<--| ENTER] key to quit")
    quit()

def find_string_in_file(file, string):
    """
    find_string_in_file(file, string)

    Description: Find string in text file.

    Arguments:
    file: the input text file
    string: the string you want to find in the file.

    Results should print as the file name, the line number, and the string itself.
    """
    linenum = 0
    with open(file, 'r') as infile:
        lines = infile.readlines()
    for l in lines:
        linenum+= 1
        if str(string) in l:
            print_string = f"In File {file}, Line Number {linenum} String: {l}"
            print(print_string)

def curdir():
    cwd = os.getcwd()
    return cwd