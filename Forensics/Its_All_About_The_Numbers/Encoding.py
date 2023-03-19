from PIL import Image
import numpy as np

img_original = Image.open(r"Images_Used/Original.jpg")
magic_square = Image.open(r"Images_Used/Magic.png")
magic_matrix = np.array(magic_square, dtype = 'uint8')
img_original_matrix = np.array(img_original, dtype = 'uint8')

for i in range(300):
    for j in range(300):

            if magic_matrix[i][j][0] == 255:

                if img_original_matrix[i][j][0] % 2 == 1:
                    continue
                else:
                    img_original_matrix[i][j][0] += 1

            else:

                if img_original_matrix[i][j][0] % 2 == 0:
                    continue
                else:
                    img_original_matrix[i][j][0] += 1


img = Image.fromarray(img_original_matrix)
img.save('Encoded_Image.png')
                