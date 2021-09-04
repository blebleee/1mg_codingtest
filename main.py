import os
import requests
import json
import time 
import io 
from io import BytesIO

from PIL import Image
import cv2 
import numpy as np 

import pytesseract

from flask import Flask, flash, request, redirect, url_for, render_template, send_file

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def main():
    
    if request.method == 'POST':
        # remove image in static folder
        for i in range(1, 5):
            img_name = 'static/img' + str(i) + '.png'
            if os.path.exists(img_name):
                os.remove(img_name)

        res = ['', '', '', '']
        img_name = ['', '', '', '']

        if request.files['img1'].filename == '':
            res[0] = 'No image'
        else:
            name = 'static/img1.png'
            img1 = Image.open(request.files['img1'])
            img1.save(name)
            img_name[0] = name
            text = pytesseract.image_to_string(img1, config='--psm 10 --oem 1 -c tessedit_char_whitelist=0123456789')
            if not text:
                res[0] = ''
            else:
                res[0] = text[0]

        if request.files['img2'].filename == '':
            res[1] = 'No image'
        else:
            name = 'static/img2.png'
            img2 = Image.open(request.files['img2'])
            img2.save(name)
            img_name[1] = name
            text = pytesseract.image_to_string(img2, config='--psm 10 --oem 1 -c tessedit_char_whitelist=0123456789')
            if not text:
                res[1] = ''
            else:
                res[1] = text[0]

        if request.files['img3'].filename == '':
            res[2] = 'No image'
        else:
            name = 'static/img3.png'
            img3 = Image.open(request.files['img3'])
            img3.save(name)
            img_name[2] = name
            text = pytesseract.image_to_string(img3, config='--psm 10 --oem 1 -c tessedit_char_whitelist=0123456789')
            if not text:
                res[2] = ''
            else:
                res[2] = text[0]

        if request.files['img4'].filename == '':
            res[3] = 'No image'
        else:
            name = 'static/img4.png'
            img4 = Image.open(request.files['img4'])
            img4.save(name)
            img_name[3] = name
            text = pytesseract.image_to_string(img4, config='--psm 10 --oem 1 -c tessedit_char_whitelist=0123456789')
            if not text:
                res[3] = ''
            else:
                res[3] = text[0]
        return render_template('main.html', res=res, img_name=img_name)


    return render_template('main.html')

app.run('0.0.0.0', port=8888)

