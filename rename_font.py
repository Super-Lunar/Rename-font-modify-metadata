from fontTools.ttLib import TTFont

def rename_font(input_font_path, output_font_path, new_name):
    try:
        # Open the font file
        font = TTFont(input_font_path)

        # Access the 'name' table
        name_table = font['name']

        # Iterate through name records and change the name
        for record in name_table.names:
            if record.nameID in [1, 4, 6]:  # 1: Font Family, 4: Full Font Name, 6: PostScript Name
                old_value = record.toStr()
                record.string = new_name.encode('utf-16-be') if b'\x00' in record.string else new_name.encode('utf-8')
                print(f"Renamed {old_value} to {new_name}")

        # Save the modified font
        font.save(output_font_path)
        print(f"Font renamed and saved as: {output_font_path}")
    except Exception as e:
        print(f"Error: {e}")

# Input and output font paths
input_font_path = "genshinfont.ttf"  # Replace with the path to your font file
output_font_path = "genshin-font.ttf" #replace with your new font name
new_name = "genshin-font" #this is what it is saved as while installing

# Rename the font
rename_font(input_font_path, output_font_path, new_name)
