from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = 'C:/Windows/Fonts/arial.ttf'

def make_favicon(size, font_size, filepath):
    img = Image.new('RGBA', (size, size), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, font_size)

    # Measure CEEP as one unit for natural letter spacing
    ce_box  = draw.textbbox((0, 0), 'CE',   font=font)
    ceep_box = draw.textbbox((0, 0), 'CEEP', font=font)

    tw = ceep_box[2] - ceep_box[0]
    th = ceep_box[3] - ceep_box[1]
    x  = (size - tw) // 2 - ceep_box[0]
    y  = (size - th) // 2 - ceep_box[1]

    ce_w = ce_box[2] - ce_box[0]

    draw.text((x,        y), 'CE', font=font, fill=(17,  17,  17,  255))
    draw.text((x + ce_w, y), 'EP', font=font, fill=(192, 82,  40,  255))

    img.save(filepath, 'PNG')
    print(f'Saved {filepath}  ({size}x{size}, font {font_size}px)')

make_favicon(32,  14, 'favicon.png')
make_favicon(180, 78, 'apple-touch-icon.png')
print('Done.')
