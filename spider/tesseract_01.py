import pytesseract
from PIL import Image

image = Image.open('./111.jpg')

text = pytesseract.image_to_string(image)
print(text)