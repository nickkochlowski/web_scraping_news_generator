""" This function takes a path to an image as a parameter, and adds a vertical
gradient in order to make overlaying text more visible. """

from PIL import Image

def gradient_photo(path):
    im = Image.open(path)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    width, height = im.size
    gradient = Image.new('L', (1, height), color=0xFF)
    for x in range(height):
        y = int(1.3*(x-380))
        if(x>380):
            gradient.putpixel((0, x), y)
        else:
            gradient.putpixel((0, x), 0)
    alpha = gradient.resize(im.size)
    black_im = Image.new('RGBA', (width, height), color=0) # i.e. black
    black_im.putalpha(alpha)
    gradient_im = Image.alpha_composite(im, black_im)
    gradient_im.save(path, 'PNG', subsampling=0, quality=100)
