from PIL import Image
import glob

JPGs = glob.glob('*.jpg')
PDFs = glob.glob('*.pdf')

for JPG in JPGs:
    name = JPG.replace('.jpg', '')
    print(JPG)
    image = Image.open(JPG)
    
    # Convert image to RGB if it's not already, as PDF doesn't support alpha channel (transparency)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    pdf_path = f"{name}.pdf"
    
    if pdf_path not in PDFs:
        image.save(pdf_path, "PDF")