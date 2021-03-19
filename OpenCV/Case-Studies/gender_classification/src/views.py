import os
from flask import Flask
from flask import render_template, request, redirect, url_for
from PIL import Image

from utils import cleanfile, pipeline_model

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
UPLOAD_FOLDER = os.path.join(path, 'static/uploads')

def base():
   return render_template('base.html')

def homepage():
   return render_template('index.html')

def getwidth(path):
   img = Image.open(path)
   size = img.size
   aspect = size[0] / size[1]
   if aspect > 1.0:
      w = 350 * aspect
   else:
      w = 350
   return int(w)

def faceapp():
   if request.method == 'POST':
      f = request.files['image']
      filename = f.filename
      upload_path = os.path.join(UPLOAD_FOLDER, filename)
      f.save(upload_path)
      # cleaning
      cleanfile(path, filename)
      # processing
      w = getwidth(upload_path)
      # prediction
      pipeline_model(upload_path, filename, color='BGR')
      return render_template('faceapp.html', fileupload=True, img_name=filename, w=w)

   return render_template('faceapp.html', fileupload=False, img_name='fitpet_logo.png', w=350)