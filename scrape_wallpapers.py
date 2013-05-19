#!/usr/bin/python
from requests import get
from random import choice
from os import makedirs, path
from re import match
from urllib import quote
from gi.repository.Gio import Settings

def main():
    page = get("http://reddit.com/r/wallpapers+wallpaper/.json")
    pattern = r'.*[jp][pn]g$'   
    while True:
        img = choice(page.json()['data']['children'])
        pics = match(pattern, img['data']['url'].lower())
        if not pics:
            continue
        else:
            directory = path.expanduser('~') + '/Pictures/Wallpapers'
            if not path.exists(directory):
                makedirs(directory)
            path_to_file = directory + '/' + img['data']['url'].split("/")[-1]
            pic_file = get(img['data']['url'])
            with open(path_to_file, 'w') as out_file:
                out_file.write(pic_file.content)
            set_background(path_to_file)
        break

def set_background(image_path, check_exist=True):
    if check_exist:
        with open(image_path, 'rb') as f:
            f.read(1)

    path_to_file = path.abspath(image_path)
    if isinstance(path_to_file, unicode):
        path_to_file = path_to_file.encode('utf-8')
    uri = 'file://' + quote(path_to_file)

    bg_setting = Settings.new('org.gnome.desktop.background')
    bg_setting.set_string('picture-uri', uri)
    bg_setting.apply()

def get_best():
    
    page = get("http://reddit.com/r/wallpapers+wallpaper/.json")
    page = page.json()['data']['children']
    score = []
    for i in page:
        score.append(i['data']['score'])
    directory = path.expanduser('~') + '/Pictures/Wallpapers'
    if not path.exists(directory):
        makedirs(directory)
    best_link = page[score.index(max(score))]['data']['url']
    path_to_file = directory + '/' + best_link.split("/")[-1]
    best_pic_file = get(best_link)
    with open(path_to_file, 'w') as out_file:
        out_file.write(best_pic_file.content)
    set_background(path_to_file)
    
if __name__ == "__main__":
    main()
