To rename a font file's internal name (metadata), you can use the fonttools library, which provides tools for working with fonts. Below is a Python script to rename the internal font name 

Prerequisites:
Install the fonttools library:

pip install fonttools


# Input and output font paths
input_font_path = "genshinfont.ttf"  # Replace with the path to your font file
output_font_path = "genshin-font.ttf" #replace with your new font name
new_name = "genshin-font" #this is what it is saved as while installing

How It Works:
The script uses the fontTools.ttLib module to open and modify the font.
The name table in the font file stores metadata such as the font's family name, full name, and PostScript name.
It updates the nameID values:
Font Family Name.
Full Font Name.
PostScript Name.
The modified font is saved as a new file with the updated name.


Instructions:
Replace "genshinfont.ttf" with the path to your existing font file.
Run the script.
A new file, genshin-font.ttf, will be created with the updated internal name.
Let me know if you need help executing it!
