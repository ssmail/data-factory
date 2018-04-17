import time

from PIL import Image
from aip import AipOcr


def gif2png(image):
    img = Image.open(image)
    img.save(image + '.png', 'png', optimize=True, quality=70)


def image2str(image):
    img = get_file_content(image)

    APP_ID = '11105809'
    API_KEY = 'G3rShuQZkzdfvWwakQriprrK'
    SECRET_KEY = 'IMxycL1pKH1Q9UdE7jRfea38ZIwyP5G2'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    options = {}
    options["language_type"] = "ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "false"
    resp = client.basicGeneral(img, options)
    print resp
    return resp['words_result'][0]['words'].replace(" ", "")


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
