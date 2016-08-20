"""
Description: Python web spider script to get the HD image from 1x.com website
Author: Mohamed Abuelanin
Contact : mohamed.abuelanin@gmail.com
"""


import requests

url = raw_input("Enter Image URL -Enter Space after the URI-\n")
src = requests.get(url).content

def get_image(src):
    for i in range(len(src)):
        if src[i:i + 15] == 'rel="image_src"':
            start = i
            for x in range(i,len(src)):
                if src[x:x+7] == '-sq.jpg':
                    return src[i+22:x]+"-hd2.jpg"


print "Image Link: " + get_image(src)
