from PIL import Image, ImageDraw
from io import BytesIO


def get_element_image(driver, element):
    location = element.location
    size = element.size

    png = driver.get_screenshot_as_png()  # saves screenshot of entire page

    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left * 2, top * 2, right * 2, bottom * 2))  # defines crop points

    im.save('screenshot.png')  # saves new cropped image


def draw_rectangle(fp, start, end, new_file=True, color=True, new_name="", bold=10):
    """
    Usage:
        draw a rectangle on a image file

    :param fp: the image file path
    :param start: the left-top corner point (x, y)
    :param end: the right-bottom corner point (x, y)
    :param new_file: the new file path
    :param color: the rectangle edge color
    just two colors, if True Blue else Red
    :param new_name: if True, draw rectangle on a new image
    :param bold: rectangle edge bold, default is 10
    :return: the image file path which be draw
    """
    img_path = new_name if new_file else fp
    RGB = 'blue' if color else 'red'
    source_img = Image.open(fp)
    draw = ImageDraw.Draw(source_img)
    outline_width = bold
    draw.line((start, (start[0], end[1]), end), fill=RGB, width=outline_width)
    draw.line((start, (end[0], start[1]), end), fill=RGB, width=outline_width)
    source_img.save(img_path, "png")
    return img_path


