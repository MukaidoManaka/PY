import requests

def IF(words):
    url = "http://www.wdylike.appspot.com/?q=" + words
    res = requests.get(url).text
    print('返回内容',res)
    if res == 'false':
        print("很文明")
    else:
        print("you 脏话")

f = open("./browserSearch.txt")
str = f.read()
f.close()
IF(str)