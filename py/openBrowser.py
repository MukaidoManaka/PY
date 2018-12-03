import webbrowser
import threading
import time

def openURL(url):
    webbrowser.open(url)
    # os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://www.youtube.com/watch?v=lSnOoN8a1Mc')

url = 'https://www.youtube.com/watch?v=lSnOoN8a1Mc'

for i in range(5):
    if i < 5:
        threading.Timer(0,openURL(url))
        time.sleep(10)
        # timer.start()
        
        f = open('url.txt','a')
        f.write('第'+ str(i) + '次写入:' + url +'\n')    #can only concatenate str (not "int") to str

f.close() #不知道在for外关闭有用没