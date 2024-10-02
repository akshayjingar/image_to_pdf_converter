from PIL import Image
import pytesseract
from googletrans import Translator
from fpdf import FPDF
from deep_translator import GoogleTranslator

# Initialize tanslator and pdf

translator = Translator()
pdf = FPDF()

#list of image files
images = ['image1.jpg']



for image in images:
    img = Image.open(image)
    text = pytesseract.image_to_string(img,lang='guj')

    translation = GoogleTranslator(source='gu', target='en').translate(text)

    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, translation)

# Save PDF
pdf.output("translated_book1.pdf")