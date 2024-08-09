from PIL import Image, ImageDraw, ImageFont
import os
import math

def image_grid(imgs, rows, cols):
    w,h = imgs[0].size
    if (rows == 0):
        rows = int(math.ceil(len(imgs)/cols))
    grid = Image.new('RGB', size=(cols*w, rows*h))
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

path = os.path.dirname(__file__)

font = ImageFont.truetype(path + '/Roboto-Regular.ttf', 24)

def img_with_text(img, s):
   tmp = img.copy()
   im = ImageDraw.Draw(tmp)
   im.text((15,15), s, (0,0,0), font=font, stroke_width=1, stroke_fill=(255,255,255))
   return tmp


