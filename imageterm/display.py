from io import BytesIO
import requests
from PIL import Image as PILImage
from pixcat import Image

HEADERS = {"User-Agent": "imageTerm/0.1 (https://github.com/guy5116)"}

def display(url):
    try:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        img = PILImage.open(BytesIO(r.content))
        Image(img).fit_screen().show(align="left")
    except:
        print(r"Unsupported file format, sorry :(")
