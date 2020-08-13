# Connor Sanders
# 10/27/2017

# Emoji Unicode/Symbol JSON Map File Builder
# Developed with and Tested using python 2.7 and 3.5 on Debian 9
# Returns a series of json files containing a dictionary of emoji names to an object of unicode and char values.

import os
import re
from json import dump
import time
import datetime
import requests
from bs4 import BeautifulSoup


# Declare datetime time stamp, and current working directory and file variables
dt = datetime.datetime.today()
c_dir = os.getcwd()
tar_url = 'http://www.unicode.org/emoji/charts/full-emoji-list.html'


# OS Specific Code for Cross Platform Purposes
os_system = os.name
if os_system == 'nt':
    json_out_dir = c_dir + '\\emoji_map_files\\'
else:
    json_out_dir = c_dir + '/emoji_map_files/'


# Function to retrieve and parse html from targeted website
def scrape_data(url):
    response = requests.get(url)
    time.sleep(5)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


# Function used to delete the older emoji output files
def remove_emoji_json_file():
    for filename in os.listdir(json_out_dir):
        if filename.endswith('.json'):
            os.remove(json_out_dir + filename)
            print(filename + ' has been removed!!')


# Function used to create the emoji output files
def create_emoji_json_file(filename, data_obj):
    with open(json_out_dir + filename + '.json', 'w') as json_outfile:
        dump(data_obj, json_outfile, indent=4)
    json_outfile.close()
    print(filename + '.json has been created!!')


# Function to clean returned text strings
def clean_text(text_str):
    re_clean = re.compile(r'[^0-9a-zA-Z*#_\s-]')
    precleaned_str = re_clean.sub('', text_str).strip()
    cleaned_str = precleaned_str.replace('-', ' ').replace('  ', ' ').replace(' ', '_').replace('__', '_').lower()
    return cleaned_str


# Function to build master Emoji Unicode Object
def build_data_obj():
    soup = scrape_data(tar_url)
    table_rows = soup.find_all('tr')
    data_list = []
    list_dict = {}
    sub_dict = {}
    x = 0
    y = 0
    z = 0
    for table_row in table_rows:
        big_table_header_th = table_row.find("th", {"class": "bighead"})
        med_table_header_th = table_row.find("th", {"class": "mediumhead"})
        unicode_emoji_td = table_row.find("td", {"class": "code"})
        emoji_char_td = table_row.find("td", {"class": "chars"})
        emoji_name_td = table_row.find("td", {"class": "name"})
        z += 1
        if big_table_header_th:
            if x < 1:
                cur_file = clean_text(big_table_header_th.get_text())
                x += 1
            else:
                list_dict.update({cur_section: sub_dict})
                data_list.append({cur_file: list_dict})
                list_dict = {}
                cur_file = clean_text(big_table_header_th.get_text())
                y = 0
        elif med_table_header_th:
            if y < 1:
                cur_section = clean_text(med_table_header_th.get_text())
                y += 1
            else:
                list_dict.update({cur_section: sub_dict})
                sub_dict = {}
                cur_section = clean_text(med_table_header_th.get_text())
        elif unicode_emoji_td:
            emoji_name = clean_text(emoji_name_td.get_text())
            emoji_char = emoji_char_td.get_text()
            emoji_code = unicode_emoji_td.get_text()
            sub_dict.update({emoji_name: {'unicode': emoji_code, 'js_escape': emoji_char}})
        if z == len(table_rows):
            list_dict.update({cur_section: sub_dict})
            data_list.append({cur_file: list_dict})
    return data_list


# Main Function that handles the process
def main():
    remove_emoji_json_file()
    data_list = build_data_obj()
    for list_item in data_list:
        file_hash = list(list_item.keys())[0]
        file_name = file_hash.replace('_', '_and_') + '_emoji_map'
        create_emoji_json_file(file_name, list_item[file_hash])
    print('Emoji JSON Mapping Process is Complete!')

main()
