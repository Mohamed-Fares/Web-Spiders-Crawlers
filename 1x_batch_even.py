"""
Description: Python web spider script to get the HD images from 1x.com website
Author: Mohamed Abuelanin
Contact : mohamed.abuelanin@gmail.com
"""

import requests


def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

def imageSize(url):
    r = requests.head(url,headers={'Accept-Encoding': 'identity'})
    print r.headers['content-length']
    return int(r.headers['content-length'])


def get_image(src):
    for i in range(len(src)):
        if src[i:i + 15] == 'rel="image_src"':
            for x in range(i, len(src)):
                if src[x:x+7] == '-sq.jpg':
                    return src[i+22:x]+"-hd2.jpg"
                else:
                    continue
        if(i==len(src)-1):
            return "false"

startFrom = raw_input("Start download from image no: \n")
imageNo = int(startFrom)

while 1:
    imageNo += 1
    if(imageNo%2 != 0):
        continue
    url = 'https://1x.com/photo/'+str(imageNo)+'/popular:all'
    src = requests.get(url).content

    if(get_image(src)=="false"):
        print "Image: %d Not Found" % imageNo 
        continue
    else:
        print "Image: %d Downloaded" % imageNo
        imageName=str(imageNo)+".jpg"
        src = get_image(src)
        with open(imageName,'wb') as f:
            f.write(requests.get(src).content)
            f.close()
                
        

        
