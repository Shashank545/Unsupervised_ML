import numpy as np
import matplotlib.pyplot as plt


from PIL import Image

pic = Image.open("sample_img1.jpeg")

print(type(pic))

pic_arr = np.asarray(pic)
type(pic_arr)

plt.imshow(pic_arr)