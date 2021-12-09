from itertools import chain
from time import time
import dionysus as d
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from PIL import Image
##1。取出所有黑人的数据
filename = 'D:\downloadfromGoogle\\fairface_label_train.csv'
data = pd.read_csv(filename)
data1 = data.loc[data['race'] == 'East Asian']
col1 = data1['file']
data2 = np.array(col1)
print(data2.shape)
n = len(data2)
image_arr = []
##2. 取1000个黑人数据进行flatten操作
time0 = time()
for i in range(1000):
    filename1 = 'D:\downloadfromGoogle\\' + data2[i]
    image = Image.open(filename1)
    im = np.array(image)
    im = im.reshape(-1, im.shape[-1])
    im1 = im.flatten()
    image_arr.append(im1)
images = np.array(image_arr)
print("time1:")
print(time() - time0)

print(images.shape)



##3.用PCA进行降维
time1 = time()
pca = PCA(n_components=3)
newImages = pca.fit_transform(images)
print(newImages.shape)
print(pca.explained_variance_ratio_)
print("time2:")

print(time() - time1)

##4.进行归一化
for i in range(len(newImages)):
    newImages[i] = newImages[i] / np.linalg.norm(newImages[i])

print(newImages)
##5.构建复形

time2 = time()
f = d.fill_rips(newImages, 3, 0.5)
m = d.homology_persistence(f)
dgms = d.init_diagrams(m, f)
print("time3:")
print(time() - time2)
d.plot.plot_bars(dgms[0], show=True)
d.plot.plot_bars(dgms[1], show=True)