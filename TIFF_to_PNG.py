from PIL import Image
import glob

PNGs = glob.glob('*.png')
TIFFs = glob.glob('*.tif')

for TIFF in TIFFs:
    name = TIFF.replace('.tif','')
    print(TIFF)

    if f"{name}.png" not in PNGs:
        with Image.open(TIFF) as im:
            # Save the image as a PNG
            im.save(f"{name}.png", "PNG")
            #  im.save("image_high_dpi.png", "PNG", dpi=(300,300))