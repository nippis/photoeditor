import PIL.Image
import numpy as np
import PIL.ImageEnhance

def read_image(path):
    image = PIL.Image.open(path)
    return image

def crop_to_square(image):
    if image.width > image.height:
        image2 = image.crop(((image.width-image.height)/2, 0, (image.width-image.height)/2+image.height, image.height))
    else:
        image2 = image.crop((0,(image.height-image.width)/2,image.width,(image.height-image.width)/2))
    if image2.height != image2.width:
        image2 = image2.resize((image2.height, image2.height))
    return image2

def brUp(image):
    enhancer = PIL.ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.1)
    return image

def brDown(image):
    enhancer = PIL.ImageEnhance.Brightness(image)
    image = enhancer.enhance(0.9)
    return image

def ctUp(image):
    enhancer = PIL.ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.1)
    return image

def ctDown(image):
    enhancer = PIL.ImageEnhance.Contrast(image)
    image = enhancer.enhance(0.9)
    return image
