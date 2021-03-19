import os
from flask import Flask
from flask import render_template, request, redirect, url_for

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
UPLOAD_FOLDER = os.path.join(path, 'images')

def base():
   return render_template('base.html')

def homepage():
   return render_template('index.html')

def faceapp():
   return render_template('faceapp.html')

