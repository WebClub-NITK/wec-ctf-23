from PIL import Image
import numpy as np

image = Image.open(r"Encoded_Image.png")
image_array = np.array(image, dtype = 'uint8')

magic = []

for i in range(300):
    for j in range(300):

            if image_array[i][j][0] % 2 == 0:
                magic.append(0)

            else:
                magic.append(255)



magic = np.array(magic, dtype = 'uint8')
magic = magic.reshape(300, 300)

img = Image.fromarray(magic)
img.save('Decoded_Image.png')