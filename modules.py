import pandas as pd
import requests
from pdf2image import convert_from_path, convert_from_bytes
# from wand.image import Image as wi

#download from url
def downloadImage(url,name):
    r = requests.get(url, allow_redirects=True)
    open('D:\Another\Flask\downloaded\image_'+name+'.jpg','wb').write(r.content)
    return 'got it'

#convert pdf to jpg
def convertPDF2Im(file):
    page = convert_from_path(file,500)
    result = page.save('out.jpd')
    print ("ok")
    return result

# def convertTopdf(file):
#     pdf = wi(filename=file,resolution=300)
#     pdf2Image = pdf.convert("jpg")
#     return pdf2Image

# convertPDF2Im('D:\Another\Flask\imagetopdf.pdf')

a =open('D:\Another\Flask\imagetopdf.pdf')
print(a)

# images = convert_from_path(open('D:\Another\Flask\imagetopdf.pdf','rb').read())

# im = convertTopdf('D:\Another\Flask\imagetopdf.pdf')

if __name__ == '__main__':
    print(a)
    # convertTopdf('D:\Another\Flask\imagetopdf.pdf')