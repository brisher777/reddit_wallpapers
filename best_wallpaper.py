'''
Created on 2013-05-03

@author: ben
'''

from requests import get

def get_best():
    
    page = get("http://reddit.com/r/wallpapers+wallpaper/.json")
    page = page.json()['data']['children']
    score = []
    for i in page:
        score.append(i['data']['score'])
    print page[score.index(max(score))]['data']['url']
    
if __name__ == '__main__':
    main()