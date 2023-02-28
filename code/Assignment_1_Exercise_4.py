import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import random as rd 
path = 'C:/Users/Path/Images'
print("Class 1")
for i in range(1):
    directory = path + '/1/'
    random_file=rd.choice(os.listdir(directory))
    img = mpimg.imread(directory + random_file)
    imgplot = plt.imshow(img)
    plt.show()
print("Class 0")
for i in range(1):
    directory = path + '/0/'
    random_file=rd.choice(os.listdir(directory))
    img = mpimg.imread(directory + random_file)
    imgplot = plt.imshow(img)
    plt.show()