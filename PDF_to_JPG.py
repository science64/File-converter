from pdf2image import convert_from_path
import glob

PDFs = glob.glob('*.pdf')
JPGs = glob.glob('*.jpg')

for PDF in PDFs:
    name = PDF.replace('.pdf', '')
    print(PDF)
    
    try:
        images = convert_from_path(PDF, poppler_path=r"C:\Users\Predator\Dropbox\poppler-23.05.0\Library\bin", dpi=300)
    except:
        images = convert_from_path(PDF, poppler_path=r"poppler-23.05.0\Library\bin", dpi=300)

    if f"{name}.jpg" not in JPGs:
        images[0].save(f"{name}.jpg", "JPEG")