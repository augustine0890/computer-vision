from glob import glob
from PIL import Image
import pandas as pd
import numpy as np
import cv2

female_path = glob('../data/faces/female/*.png')
male_path = glob('../data/faces/male/*.png')
path = female_path + male_path

def getSize(path):
    img = Image.open(path)
    return img.size[0]

df = pd.DataFrame(data=path, columns=['path'])
df['size'] = df['path'].apply(getSize)
# print(df.info)
# print(df.describe())
print(df['size'].plot(kind='box'))