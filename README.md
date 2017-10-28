# emoji_unicode_json_mapping
This repository contains a Python script that webscrapes all of the emojis listed on 'http://www.unicode.org/emoji/charts/full-emoji-list.html'. It then stores the emoji data in several different JSON files representing major catagories with each JSON file being broken up into smaller sub-catagories. The emoji data maps the emoji's name, unicode string, and javascript escape string together for easy use.

## Features
* Runs in Python 2.x and 3.x.
* Runs on windows, mac, and linux.
* Includes a Python Script that webscrapes the data for all of the emojis listed on 'http://www.unicode.org/emoji/charts/full-emoji-list.html'.
* Emoji data is stored in several JSON files, each representing a major Emoji category.
* These JSON files are then further subdivided into subcategories which can be hashed out as needed.
* At the most granular level, the Emoji data is stored in an object with the emoji's name, unicode string, and javascript escape string.
* JSON Maps of all emojis come included with the repository.

## Installation
* Clone this repository from github with the following command:
```R
git clone https://github.com/JECSand/emoji_unicode_json_mapping.git
```

## How to Use
1. cd into the emoji_unicode_json_mapping directory on your machine
2. Run the python script:
```R
$ python emoji_json_mapper.py
```
3. New Emoji JSON maps will be in the /emoji_map_files/ subdirectory.
