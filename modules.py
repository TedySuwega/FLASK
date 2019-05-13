import pandas as pd
import requests

#download from url
def downloadImage(url,name):
    r = requests.get(url, allow_redirects=True)
    open('D:\Another\Flask\downloaded\image_'+name+'.jpg','wb').write(r.content)
    return 'got it'