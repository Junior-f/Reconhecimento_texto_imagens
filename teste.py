from PIL import Image
import pytesseract

# Caminho para o Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Abrir a imagem
image = Image.open('inputs/2_imagens_bonitas_para_instagram.png')
image2 = Image.open('inputs/7_imagens_bonitas_para_instagram.png')
image3 = Image.open('inputs/pensador_frases_impactantes_01.png')

# Fazer OCR
text = pytesseract.image_to_string(image, lang='por')
# Fazer OCR
text2 = pytesseract.image_to_string(image2, lang='por')
# Fazer OCR
text3 = pytesseract.image_to_string(image3, lang='por')

# Salvar o resultado
with open('outputs/resultado_ocr.txt', 'w', encoding='utf-8') as f:
    f.write(text)
    
with open('outputs/resultado_ocr.txt', 'w', encoding='utf-8') as f:
    f.write(text2)
    
with open('outputs/resultado_ocr.txt', 'w', encoding='utf-8') as f:
    f.write(text3)

print(text)
print(text2)
print(text3)
