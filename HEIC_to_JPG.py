'''
You can download ImageMagick, not "MAGIC", from its official website. Here is the download link:

https://imagemagick.org/script/download.php

===================

This script will execute the magick command (which is part of ImageMagick) for each HEIC file, effectively converting each one to a PNG.

One potential issue you might face is if the magick command isn't in your system's PATH. If you run this script and see an error message like 'magick is not recognized as an internal or external command', that means you need to add ImageMagick to your system's PATH.

To add ImageMagick to your system's PATH on Windows:

Right-click on 'This PC' (or 'My Computer') in your file explorer and choose 'Properties'.
Click on 'Advanced system settings'.
Click on 'Environment Variables...'.
In the 'System variables' section, scroll down and select the variable called 'Path', then click on 'Edit...'.
In the window that pops up, click 'New' and add the path of the directory where ImageMagick is installed. This is typically C:\Program Files\ImageMagick-{version-number}.
Click 'OK' on all windows to save the changes.
You might need to restart your terminal or Python IDE for the changes to take effect. After doing this, you should be able to use the magick command from any command line on your system, including from within Python scripts using the subprocess module.

'''

import glob
import subprocess

HEICs = glob.glob('*.HEIC')
JPEGs = glob.glob('*.jpg')

for HEIC in HEICs:
    name = HEIC.replace('.HEIC', '')
    print(HEIC)

    if f"{name}.jpg" not in JPEGs:
        # Run the ImageMagick convert command
        subprocess.run(["magick", HEIC, "-quality", "75", f"{name}.jpg"])