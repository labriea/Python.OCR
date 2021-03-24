# Import libraries
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os

#PDF2Image needs poppler : https://github.com/Belval/pdf2image -> https://github.com/oschwartz10612/poppler-windows/releases/

pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'

# Path of the pdf
PDF_file = sys.argv[1]


print("OCR on file",PDF_file)
# Store all the pages of the PDF in a variable
print("    Conversion from PDF to JPG")
pages = convert_from_path(PDF_file, 500,poppler_path = r"D:\Tools\poppler-21.03.0\Library\bin" )

# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
print("    Saving every pages to single image")
for page in pages:
	filename = "page_"+str(image_counter)+".jpg"
	page.save(filename, 'JPEG')
	image_counter = image_counter + 1


# Variable to get count of total number of pages
filelimit = image_counter-1

# Creating a text file to write the output
outfile = PDF_file[:-len(PDF_file.split('.')[-1:][0])]+'txt'

# Open the file in append mode so that
# All contents of all images are added to the same file
f = open(outfile, "a")

print("    OCR each image")
# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
	filename = "page_"+str(i)+".jpg"
	text = str(((pytesseract.image_to_string(Image.open(filename)))))
	os.remove(filename)
	#text = text.replace('-\n', '')	
	f.write(text)

f.close()
