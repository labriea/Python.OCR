#python -m pip install --upgrade pip
#python -m pip install pytesseract
#python -m pip install pillow
#python -m pip install pyperclip
#needs tesseract binaries can be downloaded from https://digi.bib.uni-mannheim.de/tesseract/

import pytesseract
import pyperclip
from PIL import ImageGrab

#define tesseract exe location
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'

img = ImageGrab.grabclipboard()
out_below = pytesseract.image_to_string(img)
pyperclip.copy(out_below)
#print('done')



