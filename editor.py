import PIL.Image
import numpy as np

image_path = "Image 12.jpg"

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


