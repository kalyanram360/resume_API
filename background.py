from rembg import remove
from PIL import Image


input_image = Image.open(r"C:\Users\KALYAN\Pictures\Screenshots\Screenshot 2025-02-02 162805.png")
output_image = remove(input_image)
output_image.save("output.png")

